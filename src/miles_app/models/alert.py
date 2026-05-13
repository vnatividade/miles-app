from datetime import date, datetime

from sqlalchemy import (
    JSON,
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    Integer,
    Numeric,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from miles_app.core.db import Base


class Alert(Base):
    __tablename__ = "alerts"
    __table_args__ = (
        CheckConstraint("end_date >= start_date", name="ck_alerts_date_range"),
        CheckConstraint("flexibility_days >= 0", name="ck_alerts_flexibility_days"),
        CheckConstraint("passengers >= 1", name="ck_alerts_passengers"),
        CheckConstraint("max_miles > 0", name="ck_alerts_max_miles"),
        CheckConstraint(
            "max_cash_fee IS NULL OR max_cash_fee >= 0",
            name="ck_alerts_max_cash_fee",
        ),
        CheckConstraint("frequency_minutes >= 15", name="ck_alerts_frequency_minutes"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    origin_airport: Mapped[str] = mapped_column(String(3), nullable=False)
    destination_airport: Mapped[str] = mapped_column(String(3), nullable=False)
    destination_city: Mapped[str | None] = mapped_column(String(120), nullable=True)
    destination_country: Mapped[str | None] = mapped_column(String(120), nullable=True)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    flexibility_days: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    cabin_class: Mapped[str] = mapped_column(String(32), nullable=False)
    passengers: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    max_miles: Mapped[int] = mapped_column(Integer, nullable=False)
    max_cash_fee: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    programs: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    nonstop_only: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    frequency_minutes: Mapped[int] = mapped_column(Integer, default=60, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, index=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
