from typing import Annotated

from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, ConfigDict, Field

from miles_app.api.dependencies import get_program_service
from miles_app.services import ProgramService


class ProgramCreateRequest(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=120,
        examples=["Smiles"],
        description="Loyalty program display name.",
    )


class ProgramResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="Internal program identifier.")
    name: str = Field(description="Loyalty program display name.")


ProgramServiceDependency = Annotated[ProgramService, Depends(get_program_service)]

router = APIRouter(prefix="/programs", tags=["programs"])


@router.post(
    "",
    response_model=ProgramResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create loyalty program",
    description="Create a loyalty program record in the local persistence layer.",
    responses={
        status.HTTP_201_CREATED: {"description": "Program created."},
        422: {"description": "Invalid program payload."},
    },
)
def create_program(
    payload: ProgramCreateRequest,
    service: ProgramServiceDependency,
) -> ProgramResponse:
    return ProgramResponse.model_validate(service.create_program(name=payload.name))


@router.get(
    "",
    response_model=list[ProgramResponse],
    summary="List loyalty programs",
    description="List loyalty program records from the local persistence layer.",
    responses={status.HTTP_200_OK: {"description": "Programs returned."}},
)
def list_programs(service: ProgramServiceDependency) -> list[ProgramResponse]:
    return [ProgramResponse.model_validate(program) for program in service.list_programs()]
