from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from miles_app.core.db import Base
from miles_app.repositories.program_repository import SqlAlchemyProgramRepository


def test_program_repository_create_and_list() -> None:
    engine = create_engine("sqlite+pysqlite:///:memory:", future=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        repository = SqlAlchemyProgramRepository(session)

        created = repository.create("Smiles")
        listed = repository.list_all()

    assert created.id == 1
    assert created.name == "Smiles"
    assert len(listed) == 1
    assert listed[0].name == "Smiles"
