from collections.abc import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from miles_app.core.db import Base, get_db_session
from miles_app.main import create_app


@pytest.fixture
def app_with_database() -> Generator[FastAPI, None, None]:
    # Arrange
    engine = create_engine(
        "sqlite+pysqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )
    Base.metadata.create_all(engine)

    def override_get_db_session() -> Generator[Session, None, None]:
        with Session(engine) as session:
            yield session

    app = create_app()
    app.dependency_overrides[get_db_session] = override_get_db_session

    yield app

    app.dependency_overrides.clear()
    Base.metadata.drop_all(engine)


def _alert_payload() -> dict[str, object]:
    return {
        "user_id": 1,
        "origin_airport": "gru",
        "destination_airport": "mia",
        "destination_city": "Miami",
        "destination_country": "United States",
        "start_date": "2026-06-01",
        "end_date": "2026-06-15",
        "flexibility_days": 2,
        "cabin_class": "economy",
        "passengers": 2,
        "max_miles": 55000,
        "max_cash_fee": 250.00,
        "programs": ["Smiles", "Azul"],
        "nonstop_only": True,
        "frequency_minutes": 120,
        "active": True,
    }


def test_alerts_can_be_created_listed_read_updated_and_deleted(
    app_with_database: FastAPI,
) -> None:
    # Arrange
    client = TestClient(app_with_database)

    # Act
    create_response = client.post("/alerts", json=_alert_payload())
    list_response = client.get("/alerts", params={"user_id": 1})
    get_response = client.get("/alerts/1")
    update_response = client.patch("/alerts/1", json={"max_miles": 50000, "active": False})
    delete_response = client.delete("/alerts/1")
    deleted_get_response = client.get("/alerts/1")

    # Assert
    assert create_response.status_code == 201
    assert create_response.json()["origin_airport"] == "GRU"
    assert create_response.json()["destination_airport"] == "MIA"
    assert create_response.json()["programs"] == ["Smiles", "Azul"]
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1
    assert get_response.status_code == 200
    assert update_response.status_code == 200
    assert update_response.json()["max_miles"] == 50000
    assert update_response.json()["active"] is False
    assert delete_response.status_code == 204
    assert deleted_get_response.status_code == 404


def test_alert_create_rejects_invalid_date_range(app_with_database: FastAPI) -> None:
    # Arrange
    client = TestClient(app_with_database)
    payload = _alert_payload()
    payload["end_date"] = "2026-05-31"

    # Act
    response = client.post("/alerts", json=payload)

    # Assert
    assert response.status_code == 422


def test_alert_patch_rejects_invalid_existing_date_range(app_with_database: FastAPI) -> None:
    # Arrange
    client = TestClient(app_with_database)
    client.post("/alerts", json=_alert_payload())

    # Act
    response = client.patch("/alerts/1", json={"end_date": "2026-05-31"})

    # Assert
    assert response.status_code == 422


def test_openapi_includes_alert_contract(app_with_database: FastAPI) -> None:
    # Arrange
    client = TestClient(app_with_database)

    # Act
    response = client.get("/openapi.json")

    # Assert
    assert response.status_code == 200
    assert "/alerts" in response.json()["paths"]
    assert "/alerts/{alert_id}" in response.json()["paths"]
    assert response.json()["paths"]["/alerts"]["post"]["summary"] == "Create alert"
