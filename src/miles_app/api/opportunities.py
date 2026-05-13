from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status

from miles_app.schemas.opportunities import OpportunityResponse

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
