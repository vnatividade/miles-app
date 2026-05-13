from datetime import date
from typing import Any

from miles_app.models import Alert
from miles_app.repositories.alert_repository import AlertRepository


class AlertNotFoundError(ValueError):
    pass


class AlertValidationError(ValueError):
    pass


class AlertService:
    def __init__(self, repository: AlertRepository) -> None:
        self._repository = repository

    def create_alert(self, values: dict[str, Any]) -> Alert:
        self._validate_date_range(values["start_date"], values["end_date"])
        return self._repository.create(values)

    def list_alerts(self, user_id: int | None = None) -> list[Alert]:
        return self._repository.list_all(user_id=user_id)

    def get_alert(self, alert_id: int) -> Alert:
        alert = self._repository.get_by_id(alert_id)
        if alert is None:
            raise AlertNotFoundError(f"Alert {alert_id} was not found.")
        return alert

    def update_alert(self, alert_id: int, values: dict[str, Any]) -> Alert:
        alert = self.get_alert(alert_id)
        start_date = values.get("start_date", alert.start_date)
        end_date = values.get("end_date", alert.end_date)
        self._validate_date_range(start_date, end_date)
        return self._repository.update(alert, values)

    def delete_alert(self, alert_id: int) -> None:
        alert = self.get_alert(alert_id)
        self._repository.delete(alert)

    def _validate_date_range(self, start_date: date, end_date: date) -> None:
        if end_date < start_date:
            raise AlertValidationError("end_date must be on or after start_date.")
