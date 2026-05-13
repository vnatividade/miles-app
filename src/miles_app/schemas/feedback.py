from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

FeedbackType = Literal[
    "alert_expectation",
    "notification_relevance",
    "alert_deactivation",
    "weekly_pulse",
    "manual_feedback",
]
FeedbackReason = Literal[
    "useful",
    "not_useful",
    "too_expensive",
    "bad_dates",
    "high_fees",
    "wrong_destination",
    "already_saw_this",
    "found_ticket",
    "too_many_notifications",
    "no_longer_traveling",
    "prefer_manual_search",
    "other",
]


class FeedbackCreateRequest(BaseModel):
    user_id: int = Field(gt=0, description="User submitting feedback.", examples=[1])
    alert_id: int | None = Field(
        default=None,
        gt=0,
        description="Related alert, when feedback is alert-specific.",
        examples=[1],
    )
    opportunity_id: int | None = Field(
        default=None,
        gt=0,
        description="Related opportunity, when feedback is opportunity-specific.",
        examples=[1],
    )
    feedback_type: FeedbackType = Field(
        description="Feedback capture moment.",
        examples=["notification_relevance"],
    )
    rating: int | None = Field(
        default=None,
        ge=1,
        le=5,
        description="Optional 1 to 5 rating.",
        examples=[4],
    )
    reason: FeedbackReason | None = Field(
        default=None,
        description="Optional structured feedback reason.",
        examples=["too_expensive"],
    )
    comment: str | None = Field(
        default=None,
        max_length=1000,
        description="Optional free-form feedback comment.",
        examples=["Good route, but the fees were higher than expected."],
    )


class FeedbackAcceptedResponse(BaseModel):
    status: Literal["accepted_placeholder"] = Field(
        default="accepted_placeholder",
        description="Placeholder status until feedback persistence exists.",
    )
    received_at: datetime = Field(
        description="Timestamp when the backend received the feedback.",
        examples=["2026-05-13T09:00:00Z"],
    )
    feedback: FeedbackCreateRequest = Field(description="Accepted feedback payload.")


class FeedbackSummaryResponse(BaseModel):
    total_feedback: int = Field(description="Total feedback records.", examples=[0])
    useful_count: int = Field(description="Useful feedback count.", examples=[0])
    not_useful_count: int = Field(description="Not useful feedback count.", examples=[0])
    top_reasons: list[str] = Field(
        default_factory=list,
        description="Most common structured reasons.",
        examples=[["too_expensive", "bad_dates"]],
    )
