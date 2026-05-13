from miles_app.models import LoyaltyProgram
from miles_app.repositories.program_repository import ProgramRepository


class ProgramService:
    def __init__(self, repository: ProgramRepository) -> None:
        self._repository = repository

    def create_program(self, name: str) -> LoyaltyProgram:
        return self._repository.create(name=name)

    def list_programs(self) -> list[LoyaltyProgram]:
        return self._repository.list_all()
