"""create alerts table"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "20260513_02"
down_revision: str | Sequence[str] | None = "20260513_01"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "alerts",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("origin_airport", sa.String(length=3), nullable=False),
        sa.Column("destination_airport", sa.String(length=3), nullable=False),
        sa.Column("destination_city", sa.String(length=120), nullable=True),
        sa.Column("destination_country", sa.String(length=120), nullable=True),
        sa.Column("start_date", sa.Date(), nullable=False),
        sa.Column("end_date", sa.Date(), nullable=False),
        sa.Column("flexibility_days", sa.Integer(), nullable=False),
        sa.Column("cabin_class", sa.String(length=32), nullable=False),
        sa.Column("passengers", sa.Integer(), nullable=False),
        sa.Column("max_miles", sa.Integer(), nullable=False),
        sa.Column("max_cash_fee", sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column("programs", sa.JSON(), nullable=False),
        sa.Column("nonstop_only", sa.Boolean(), nullable=False),
        sa.Column("frequency_minutes", sa.Integer(), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.CheckConstraint("end_date >= start_date", name="ck_alerts_date_range"),
        sa.CheckConstraint("flexibility_days >= 0", name="ck_alerts_flexibility_days"),
        sa.CheckConstraint("passengers >= 1", name="ck_alerts_passengers"),
        sa.CheckConstraint("max_miles > 0", name="ck_alerts_max_miles"),
        sa.CheckConstraint(
            "max_cash_fee IS NULL OR max_cash_fee >= 0",
            name="ck_alerts_max_cash_fee",
        ),
        sa.CheckConstraint("frequency_minutes >= 15", name="ck_alerts_frequency_minutes"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_alerts_active"), "alerts", ["active"], unique=False)
    op.create_index(op.f("ix_alerts_user_id"), "alerts", ["user_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_alerts_user_id"), table_name="alerts")
    op.drop_index(op.f("ix_alerts_active"), table_name="alerts")
    op.drop_table("alerts")
