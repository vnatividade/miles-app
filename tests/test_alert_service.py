from datetime import date

import pytest

from miles_app.models import Alert
from miles_app.services import AlertNotFoundError, AlertService, AlertValidationError


class InMemoryAlertRepository:
    def __init__(self) -> None:
        self.alerts: dict[int, Alert] = {}
        self.next_id = 1

    def create(self, values: dict[str, object]) -> Alert:
        alert = Alert(**values)
        alert.id = self.next_id
        self.alerts[alert.id] = alert
        self.next_id += 1
        return alert

    def list_all(self, user_id: int | None = None) -> list[Alert]:
        alerts = list(self.alerts.values())
        if user_id is not None:
            return [alert for alert in alerts if alert.user_id == user_id]
        return alerts

    def get_by_id(self, alert_id: int) -> Alert | None:
        return self.alerts.get(alert_id)

    def update(self, alert: Alert, values: dict[str, object]) -> Alert:
        for field, value in values.items():
            setattr(alert, field, value)
        return alert

    def delete(self, alert: Alert) -> None:
        del self.alerts[alert.id]


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


def test_alert_service_updates_existing_alert() -> None:
    # Arrange
    repository = InMemoryAlertRepository()
    service = AlertService(repository)
    alert = service.create_alert(_alert_values())

    # Act
    updated = service.update_alert(alert.id, {"max_miles": 50000, "active": False})

    # Assert
    assert updated.max_miles == 50000
    assert updated.active is False


def test_alert_service_rejects_invalid_updated_date_range() -> None:
    # Arrange
    repository = InMemoryAlertRepository()
    service = AlertService(repository)
    alert = service.create_alert(_alert_values())

    # Act / Assert
    with pytest.raises(AlertValidationError):
        service.update_alert(alert.id, {"end_date": date(2026, 5, 31)})


def test_alert_service_raises_for_missing_alert() -> None:
    # Arrange
    service = AlertService(InMemoryAlertRepository())

    # Act / Assert
    with pytest.raises(AlertNotFoundError):
        service.get_alert(999)
