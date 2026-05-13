from datetime import date, datetime
from typing import Annotated, Any, Literal

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from miles_app.api.dependencies import get_alert_service
from miles_app.services import AlertNotFoundError, AlertService, AlertValidationError

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


AlertServiceDependency = Annotated[AlertService, Depends(get_alert_service)]

router = APIRouter(prefix="/alerts", tags=["alerts"])


def _validation_error_response(exc: AlertValidationError) -> HTTPException:
    return HTTPException(status_code=422, detail=str(exc))


def _not_found_response(exc: AlertNotFoundError) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.post(
    "",
    response_model=AlertResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create alert",
    description="Create a mileage flight monitoring alert configuration.",
    responses={
        status.HTTP_201_CREATED: {"description": "Alert created."},
        422: {"description": "Invalid alert payload."},
    },
)
def create_alert(
    payload: AlertCreateRequest,
    service: AlertServiceDependency,
) -> AlertResponse:
    try:
        alert = service.create_alert(payload.model_dump())
    except AlertValidationError as exc:
        raise _validation_error_response(exc) from exc
    return AlertResponse.model_validate(alert)


@router.get(
    "",
    response_model=list[AlertResponse],
    summary="List alerts",
    description="List alert configurations, optionally filtered by user identifier.",
    responses={status.HTTP_200_OK: {"description": "Alerts returned."}},
)
def list_alerts(
    service: AlertServiceDependency,
    user_id: Annotated[int | None, Query(gt=0, description="Optional user filter.")] = None,
) -> list[AlertResponse]:
    return [AlertResponse.model_validate(alert) for alert in service.list_alerts(user_id=user_id)]


@router.get(
    "/{alert_id}",
    response_model=AlertResponse,
    summary="Get alert",
    description="Get a single alert configuration by identifier.",
    responses={
        status.HTTP_200_OK: {"description": "Alert returned."},
        status.HTTP_404_NOT_FOUND: {"description": "Alert not found."},
    },
)
def get_alert(alert_id: int, service: AlertServiceDependency) -> AlertResponse:
    try:
        alert = service.get_alert(alert_id)
    except AlertNotFoundError as exc:
        raise _not_found_response(exc) from exc
    return AlertResponse.model_validate(alert)


@router.patch(
    "/{alert_id}",
    response_model=AlertResponse,
    summary="Update alert",
    description="Partially update an existing alert configuration.",
    responses={
        status.HTTP_200_OK: {"description": "Alert updated."},
        status.HTTP_404_NOT_FOUND: {"description": "Alert not found."},
        422: {"description": "Invalid alert update."},
    },
)
def update_alert(
    alert_id: int,
    payload: AlertUpdateRequest,
    service: AlertServiceDependency,
) -> AlertResponse:
    values: dict[str, Any] = payload.model_dump(exclude_unset=True)
    try:
        alert = service.update_alert(alert_id, values)
    except AlertNotFoundError as exc:
        raise _not_found_response(exc) from exc
    except AlertValidationError as exc:
        raise _validation_error_response(exc) from exc
    return AlertResponse.model_validate(alert)


@router.delete(
    "/{alert_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete alert",
    description="Delete an alert configuration.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Alert deleted."},
        status.HTTP_404_NOT_FOUND: {"description": "Alert not found."},
    },
)
def delete_alert(alert_id: int, service: AlertServiceDependency) -> Response:
    try:
        service.delete_alert(alert_id)
    except AlertNotFoundError as exc:
        raise _not_found_response(exc) from exc
    return Response(status_code=status.HTTP_204_NO_CONTENT)
