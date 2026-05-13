from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status

from miles_app.schemas.notifications import NotificationResponse, NotificationStatusUpdateRequest

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
