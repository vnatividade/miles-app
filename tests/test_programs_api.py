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


def test_programs_can_be_created_and_listed(app_with_database: FastAPI) -> None:
    client = TestClient(app_with_database)

    create_response = client.post("/programs", json={"name": "Smiles"})
    list_response = client.get("/programs")

    assert create_response.status_code == 201
    assert create_response.json() == {"id": 1, "name": "Smiles"}
    assert list_response.status_code == 200
    assert list_response.json() == [{"id": 1, "name": "Smiles"}]


def test_openapi_includes_program_contract(app_with_database: FastAPI) -> None:
    client = TestClient(app_with_database)

    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert "/health" in response.json()["paths"]
    assert "/programs" in response.json()["paths"]
