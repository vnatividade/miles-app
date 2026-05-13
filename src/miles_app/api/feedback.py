from datetime import UTC, datetime

from fastapi import APIRouter, status

from miles_app.schemas.feedback import (
    FeedbackAcceptedResponse,
    FeedbackCreateRequest,
    FeedbackSummaryResponse,
)

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.post(
    "",
    response_model=FeedbackAcceptedResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Capture feedback",
    description=(
        "Accept frontend feedback for the MVP learning loop. "
        "This endpoint defines the contract and echoes the payload until feedback "
        "persistence exists."
    ),
    responses={
        status.HTTP_202_ACCEPTED: {"description": "Feedback accepted by placeholder contract."},
        422: {"description": "Invalid feedback payload."},
    },
)
def create_feedback(payload: FeedbackCreateRequest) -> FeedbackAcceptedResponse:
    return FeedbackAcceptedResponse(
        received_at=datetime.now(UTC),
        feedback=payload,
    )


@router.get(
    "/summary",
    response_model=FeedbackSummaryResponse,
    summary="Get feedback summary",
    description=(
        "Return aggregate feedback signals for frontend MVP display. "
        "Returns zero-state metrics until feedback persistence and analysis exist."
    ),
    responses={status.HTTP_200_OK: {"description": "Feedback summary returned."}},
)
def get_feedback_summary() -> FeedbackSummaryResponse:
    return FeedbackSummaryResponse(
        total_feedback=0,
        useful_count=0,
        not_useful_count=0,
        top_reasons=[],
    )
