from datetime import datetime
from typing import Annotated, Literal

from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field

NotificationChannel = Literal["email"]
NotificationStatus = Literal[
    "pending",
    "sent",
    "delivered",
    "opened",
    "clicked",
    "failed",
    "dismissed",
]


class NotificationResponse(BaseModel):
    id: int = Field(description="Internal notification identifier.", examples=[1])
    user_id: int = Field(description="User that owns the notification.", examples=[1])
    alert_id: int | None = Field(
        default=None,
        description="Related alert, when available.",
        examples=[1],
    )
    opportunity_id: int | None = Field(
        default=None,
        description="Related opportunity, when available.",
        examples=[1],
    )
    channel: NotificationChannel = Field(description="Notification channel.", examples=["email"])
    status: NotificationStatus = Field(
        description="Delivery or interaction status.",
        examples=["sent"],
    )
    sent_at: datetime | None = Field(
        default=None,
        description="Timestamp when notification was sent.",
        examples=["2026-05-13T09:00:00Z"],
    )
    subject: str | None = Field(
        default=None,
        description="Notification subject or headline.",
        examples=["GRU to MIA for 55,000 miles"],
    )


class NotificationStatusUpdateRequest(BaseModel):
    status: Literal["opened", "clicked", "dismissed"] = Field(
        description="Frontend-visible notification interaction status.",
        examples=["opened"],
    )


router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get(
    "",
    response_model=list[NotificationResponse],
    summary="List notifications",
    description=(
        "List user notifications for the frontend MVP. "
        "Returns an empty list until notification persistence exists."
    ),
    responses={status.HTTP_200_OK: {"description": "Notifications returned."}},
)
def list_notifications(
    user_id: Annotated[int | None, Query(gt=0, description="Optional user filter.")] = None,
) -> list[NotificationResponse]:
    _ = user_id
    return []


@router.patch(
    "/{notification_id}/status",
    response_model=NotificationResponse,
    summary="Update notification status",
    description=(
        "Update frontend-visible notification interaction status. "
        "Notification persistence is not implemented yet, so unknown IDs return 404."
    ),
    responses={
        status.HTTP_200_OK: {"description": "Notification status updated."},
        status.HTTP_404_NOT_FOUND: {"description": "Notification not found."},
        422: {"description": "Invalid notification status payload."},
    },
)
def update_notification_status(
    notification_id: int,
    payload: NotificationStatusUpdateRequest,
) -> NotificationResponse:
    _ = (notification_id, payload)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Notification not found. Notification persistence is not implemented yet.",
    )
