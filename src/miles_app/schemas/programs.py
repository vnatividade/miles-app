from pydantic import BaseModel, ConfigDict, Field


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
