from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from miles_app.core.db import Base
from miles_app.repositories.alert_repository import SqlAlchemyAlertRepository


def _alert_values() -> dict[str, object]:
    return {
        "user_id": 1,
        "origin_airport": "GRU",
        "destination_airport": "MIA",
        "destination_city": "Miami",
        "destination_country": "United States",
        "start_date": date(2026, 6, 1),
        "end_date": date(2026, 6, 15),
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


def test_alert_repository_create_list_update_and_delete() -> None:
    # Arrange
    engine = create_engine("sqlite+pysqlite:///:memory:", future=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        repository = SqlAlchemyAlertRepository(session)

        # Act
        created = repository.create(_alert_values())
        listed = repository.list_all(user_id=1)
        updated = repository.update(created, {"active": False, "max_miles": 50000})
        repository.delete(updated)
        deleted = repository.get_by_id(created.id)

    # Assert
    assert created.id == 1
    assert listed == [created]
    assert updated.active is False
    assert updated.max_miles == 50000
    assert deleted is None
