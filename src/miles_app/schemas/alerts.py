from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

CabinClass = Literal["economy", "premium_economy", "business", "first"]


class AlertBase(BaseModel):
    origin_airport: str = Field(
        min_length=3,
        max_length=3,
        examples=["GRU"],
        description="IATA origin airport code.",
    )
    destination_airport: str = Field(
        min_length=3,
        max_length=3,
        examples=["MIA"],
        description="IATA destination airport code.",
    )
    destination_city: str | None = Field(
        default=None,
        max_length=120,
        examples=["Miami"],
        description="Optional destination city label for display and filtering.",
    )
    destination_country: str | None = Field(
        default=None,
        max_length=120,
        examples=["United States"],
        description="Optional destination country label for display and filtering.",
    )
    start_date: date = Field(
        examples=["2026-06-01"],
        description="First acceptable departure date.",
    )
    end_date: date = Field(
        examples=["2026-06-15"],
        description="Last acceptable departure date.",
    )
    flexibility_days: int = Field(
        default=0,
        ge=0,
        le=30,
        examples=[2],
        description="Number of days of date flexibility around the configured range.",
    )
    cabin_class: CabinClass = Field(
        examples=["economy"],
        description="Desired cabin class.",
    )
    passengers: int = Field(
        default=1,
        ge=1,
        le=9,
        examples=[2],
        description="Number of passengers for the monitored trip.",
    )
    max_miles: int = Field(
        gt=0,
        examples=[55000],
        description="Maximum acceptable mileage price.",
    )
    max_cash_fee: float | None = Field(
        default=None,
        ge=0,
        examples=[250.00],
        description="Optional maximum acceptable cash fee.",
    )
    programs: list[str] = Field(
        min_length=1,
        examples=[["Smiles", "Azul"]],
        description="Preferred loyalty programs to monitor.",
    )
    nonstop_only: bool = Field(
        default=False,
        examples=[True],
        description="Whether only nonstop flights should match this alert.",
    )
    frequency_minutes: int = Field(
        default=60,
        ge=15,
        le=10080,
        examples=[120],
        description="Requested monitoring frequency in minutes.",
    )
    active: bool = Field(
        default=True,
        examples=[True],
        description="Whether the alert is enabled for future monitoring.",
    )

    @field_validator("origin_airport", "destination_airport", mode="before")
    @classmethod
    def normalize_airport_code(cls, value: str) -> str:
        if not isinstance(value, str):
            return value
        return value.strip().upper()

    @field_validator("programs", mode="before")
    @classmethod
    def normalize_programs(cls, value: list[str]) -> list[str]:
        if not isinstance(value, list):
            return value
        return [program.strip() for program in value if program.strip()]

    @model_validator(mode="after")
    def validate_date_range(self) -> "AlertBase":
        if self.end_date < self.start_date:
            raise ValueError("end_date must be on or after start_date.")
        return self


class AlertCreateRequest(AlertBase):
    user_id: int = Field(
        gt=0,
        examples=[1],
        description="User identifier. This remains explicit until authentication exists.",
    )


class AlertUpdateRequest(BaseModel):
    origin_airport: str | None = Field(
        default=None,
        min_length=3,
        max_length=3,
        examples=["GRU"],
        description="IATA origin airport code.",
    )
    destination_airport: str | None = Field(
        default=None,
        min_length=3,
        max_length=3,
        examples=["MIA"],
        description="IATA destination airport code.",
    )
    destination_city: str | None = Field(
        default=None,
        max_length=120,
        examples=["Miami"],
        description="Optional destination city label for display and filtering.",
    )
    destination_country: str | None = Field(
        default=None,
        max_length=120,
        examples=["United States"],
        description="Optional destination country label for display and filtering.",
    )
    start_date: date | None = Field(
        default=None,
        examples=["2026-06-01"],
        description="First acceptable departure date.",
    )
    end_date: date | None = Field(
        default=None,
        examples=["2026-06-15"],
        description="Last acceptable departure date.",
    )
    flexibility_days: int | None = Field(
        default=None,
        ge=0,
        le=30,
        examples=[2],
        description="Number of days of date flexibility around the configured range.",
    )
    cabin_class: CabinClass | None = Field(
        default=None,
        examples=["business"],
        description="Desired cabin class.",
    )
    passengers: int | None = Field(
        default=None,
        ge=1,
        le=9,
        examples=[2],
        description="Number of passengers for the monitored trip.",
    )
    max_miles: int | None = Field(
        default=None,
        gt=0,
        examples=[55000],
        description="Maximum acceptable mileage price.",
    )
    max_cash_fee: float | None = Field(
        default=None,
        ge=0,
        examples=[250.00],
        description="Optional maximum acceptable cash fee.",
    )
    programs: list[str] | None = Field(
        default=None,
        min_length=1,
        examples=[["Smiles", "Azul"]],
        description="Preferred loyalty programs to monitor.",
    )
    nonstop_only: bool | None = Field(
        default=None,
        examples=[True],
        description="Whether only nonstop flights should match this alert.",
    )
    frequency_minutes: int | None = Field(
        default=None,
        ge=15,
        le=10080,
        examples=[120],
        description="Requested monitoring frequency in minutes.",
    )
    active: bool | None = Field(
        default=None,
        examples=[False],
        description="Whether the alert is enabled for future monitoring.",
    )

    @field_validator("origin_airport", "destination_airport", mode="before")
    @classmethod
    def normalize_airport_code(cls, value: str | None) -> str | None:
        if value is None or not isinstance(value, str):
            return value
        return value.strip().upper()

    @field_validator("programs", mode="before")
    @classmethod
    def normalize_programs(cls, value: list[str] | None) -> list[str] | None:
        if value is None or not isinstance(value, list):
            return value
        return [program.strip() for program in value if program.strip()]

    @model_validator(mode="after")
    def validate_date_range(self) -> "AlertUpdateRequest":
        if self.start_date is not None and self.end_date is not None:
            if self.end_date < self.start_date:
                raise ValueError("end_date must be on or after start_date.")
        return self


class AlertResponse(AlertBase):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="Internal alert identifier.")
    user_id: int = Field(description="User identifier that owns the alert.")
    created_at: datetime = Field(description="Timestamp when the alert was created.")
    updated_at: datetime = Field(description="Timestamp when the alert was last updated.")
