from datetime import date, datetime
from typing import Annotated, Literal

from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field

CabinClass = Literal["economy", "premium_economy", "business", "first"]
OpportunityRelevanceStatus = Literal["matched", "near_match", "not_relevant", "unknown"]


class OpportunityResponse(BaseModel):
    id: int = Field(description="Internal opportunity identifier.", examples=[1])
    alert_id: int | None = Field(
        default=None,
        description="Alert that matched this opportunity, when known.",
        examples=[1],
    )
    provider: str = Field(
        description="Mileage provider that produced the result.",
        examples=["Smiles"],
    )
    airline: str | None = Field(
        default=None,
        description="Operating or marketing airline, when available.",
        examples=["GOL"],
    )
    origin: str = Field(
        min_length=3,
        max_length=3,
        description="IATA origin airport code.",
        examples=["GRU"],
    )
    destination: str = Field(
        min_length=3,
        max_length=3,
        description="IATA destination airport code.",
        examples=["MIA"],
    )
    departure_date: date = Field(description="Outbound departure date.", examples=["2026-06-01"])
    return_date: date | None = Field(
        default=None,
        description="Optional return date for round-trip opportunities.",
        examples=["2026-06-15"],
    )
    miles_price: int = Field(gt=0, description="Mileage price.", examples=[55000])
    cash_fee: float | None = Field(
        default=None,
        ge=0,
        description="Cash fee amount, when available.",
        examples=[250.00],
    )
    currency: str = Field(
        min_length=3,
        max_length=3,
        description="ISO currency code for cash fees.",
        examples=["BRL"],
    )
    cabin_class: CabinClass = Field(description="Cabin class.", examples=["economy"])
    stops: int | None = Field(
        default=None,
        ge=0,
        description="Number of stops, when known.",
        examples=[0],
    )
    flight_duration: str | None = Field(
        default=None,
        description="Human-readable flight duration, when known.",
        examples=["8h 35m"],
    )
    availability: str = Field(
        description="Provider availability status.",
        examples=["available"],
    )
    source_url: str | None = Field(
        default=None,
        description="Provider URL where the opportunity can be reviewed.",
        examples=["https://example.com/results"],
    )
    relevance_status: OpportunityRelevanceStatus = Field(
        default="unknown",
        description="Backend-owned relevance state for frontend display.",
        examples=["matched"],
    )
    captured_at: datetime = Field(
        description="Timestamp when the result was captured.",
        examples=["2026-05-13T09:00:00Z"],
    )


router = APIRouter(prefix="/opportunities", tags=["opportunities"])


@router.get(
    "",
    response_model=list[OpportunityResponse],
    summary="List opportunities",
    description=(
        "List mileage flight opportunities for the frontend MVP. "
        "Returns an empty list until scraper, normalization and matching persistence exist."
    ),
    responses={status.HTTP_200_OK: {"description": "Opportunities returned."}},
)
def list_opportunities(
    user_id: Annotated[int | None, Query(gt=0, description="Optional user filter.")] = None,
    alert_id: Annotated[int | None, Query(gt=0, description="Optional alert filter.")] = None,
) -> list[OpportunityResponse]:
    _ = (user_id, alert_id)
    return []


@router.get(
    "/{opportunity_id}",
    response_model=OpportunityResponse,
    summary="Get opportunity",
    description=(
        "Get a single mileage flight opportunity. "
        "Opportunity persistence is not implemented yet, so unknown IDs return 404."
    ),
    responses={
        status.HTTP_200_OK: {"description": "Opportunity returned."},
        status.HTTP_404_NOT_FOUND: {"description": "Opportunity not found."},
    },
)
def get_opportunity(opportunity_id: int) -> OpportunityResponse:
    _ = opportunity_id
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Opportunity not found. Opportunity persistence is not implemented yet.",
    )
