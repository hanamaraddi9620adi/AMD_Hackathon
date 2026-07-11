from uuid import uuid4

from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy import Date

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base_model import BaseModel


class Journal(BaseModel):
    """
    Trading Journal Entry
    """

    __tablename__ = "journals"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # ------------------------
    # Trade Information
    # ------------------------

    symbol: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    exchange: Mapped[str] = mapped_column(
        String(20),
        default="NSE",
    )

    trade_type: Mapped[str] = mapped_column(
        String(20),
        default="Swing",
    )

    action: Mapped[str] = mapped_column(
        String(10),
        default="BUY",
    )

    quantity: Mapped[int] = mapped_column(
        default=1,
    )

    entry_price: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    exit_price: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    pnl: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    trade_date: Mapped[Date | None] = mapped_column(
        Date,
        nullable=True,
    )

    # ------------------------
    # Journal Details
    # ------------------------

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    strategy: Mapped[str] = mapped_column(
        String(100),
        default="Swing Trading",
    )

    emotion: Mapped[str] = mapped_column(
        String(100),
        default="Neutral",
    )

    confidence: Mapped[float] = mapped_column(
        Float,
        default=5.0,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    lessons: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    ai_feedback: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    is_profitable: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )