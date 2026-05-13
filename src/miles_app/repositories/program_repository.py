from typing import Protocol

from sqlalchemy.orm import Session

from miles_app.models import LoyaltyProgram


class ProgramRepository(Protocol):
    def create(self, name: str) -> LoyaltyProgram: ...

    def list_all(self) -> list[LoyaltyProgram]: ...


class SqlAlchemyProgramRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, name: str) -> LoyaltyProgram:
        entity = LoyaltyProgram(name=name)
        self._session.add(entity)
        self._session.commit()
        self._session.refresh(entity)
        return entity

    def list_all(self) -> list[LoyaltyProgram]:
        return self._session.query(LoyaltyProgram).order_by(LoyaltyProgram.id).all()
