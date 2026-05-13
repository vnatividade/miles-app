from typing import Any, Protocol

from sqlalchemy.orm import Session

from miles_app.models import Alert


class AlertRepository(Protocol):
    def create(self, values: dict[str, Any]) -> Alert: ...

    def list_all(self, user_id: int | None = None) -> list[Alert]: ...

    def get_by_id(self, alert_id: int) -> Alert | None: ...

    def update(self, alert: Alert, values: dict[str, Any]) -> Alert: ...

    def delete(self, alert: Alert) -> None: ...


class SqlAlchemyAlertRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, values: dict[str, Any]) -> Alert:
        entity = Alert(**values)
        self._session.add(entity)
        self._session.commit()
        self._session.refresh(entity)
        return entity

    def list_all(self, user_id: int | None = None) -> list[Alert]:
        query = self._session.query(Alert)
        if user_id is not None:
            query = query.filter(Alert.user_id == user_id)
        return query.order_by(Alert.id).all()

    def get_by_id(self, alert_id: int) -> Alert | None:
        return self._session.get(Alert, alert_id)

    def update(self, alert: Alert, values: dict[str, Any]) -> Alert:
        for field, value in values.items():
            setattr(alert, field, value)
        self._session.add(alert)
        self._session.commit()
        self._session.refresh(alert)
        return alert

    def delete(self, alert: Alert) -> None:
        self._session.delete(alert)
        self._session.commit()
