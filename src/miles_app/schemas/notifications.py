from datetime import datetime
from typing import Literal

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
