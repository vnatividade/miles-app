from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from miles_app.core.db import get_db_session
from miles_app.repositories.alert_repository import AlertRepository, SqlAlchemyAlertRepository
from miles_app.repositories.program_repository import ProgramRepository, SqlAlchemyProgramRepository
from miles_app.services import AlertService, ProgramService

DbSession = Annotated[Session, Depends(get_db_session)]


def get_alert_repository(session: DbSession) -> AlertRepository:
    return SqlAlchemyAlertRepository(session)


AlertRepositoryDependency = Annotated[AlertRepository, Depends(get_alert_repository)]


def get_alert_service(repository: AlertRepositoryDependency) -> AlertService:
    return AlertService(repository)


def get_program_repository(session: DbSession) -> ProgramRepository:
    return SqlAlchemyProgramRepository(session)


ProgramRepositoryDependency = Annotated[ProgramRepository, Depends(get_program_repository)]


def get_program_service(repository: ProgramRepositoryDependency) -> ProgramService:
    return ProgramService(repository)
