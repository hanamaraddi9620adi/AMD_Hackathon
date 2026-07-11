from uuid import uuid4

from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base_model import BaseModel


class Portfolio(BaseModel):

    __tablename__ = "portfolios"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    symbol: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    exchange: Mapped[str] = mapped_column(
        String(20),
        default="NSE",
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    average_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    sector: Mapped[str] = mapped_column(
        String(100),
        default="Unknown",
    )

    notes: Mapped[str] = mapped_column(
        String(500),
        default="",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )