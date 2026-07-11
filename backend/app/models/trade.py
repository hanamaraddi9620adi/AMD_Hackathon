from uuid import uuid4

from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base_model import BaseModel


class Trade(BaseModel):
    """
    User Trade History
    """

    __tablename__ = "trades"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    symbol: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    action: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )