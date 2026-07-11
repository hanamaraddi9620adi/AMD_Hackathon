from datetime import date

from pydantic import BaseModel, Field


class JournalCreate(BaseModel):
    symbol: str = Field(..., min_length=1, max_length=20)
    exchange: str = Field(default="NSE")
    trade_type: str = Field(default="Swing")
    action: str = Field(default="BUY")

    quantity: int = Field(..., gt=0)

    entry_price: float = Field(..., gt=0)
    exit_price: float = Field(default=0)

    trade_date: date | None = None

    title: str = Field(..., min_length=3, max_length=255)

    strategy: str = Field(default="Swing Trading")

    emotion: str = Field(default="Neutral")

    confidence: float = Field(
        default=5,
        ge=0,
        le=10,
    )

    content: str = Field(...)

    lessons: str = Field(default="")


class JournalUpdate(BaseModel):

    exit_price: float | None = Field(
        default=None,
        gt=0,
    )

    pnl: float | None = None

    emotion: str | None = None

    confidence: float | None = Field(
        default=None,
        ge=0,
        le=10,
    )

    content: str | None = None

    lessons: str | None = None

    ai_feedback: str | None = None

    is_profitable: bool | None = None


class JournalResponse(BaseModel):

    id: str

    symbol: str
    exchange: str

    trade_type: str
    action: str

    quantity: int

    entry_price: float
    exit_price: float

    pnl: float

    trade_date: date | None

    title: str

    strategy: str

    emotion: str

    confidence: float

    content: str

    lessons: str

    ai_feedback: str

    is_profitable: bool

    class Config:
        from_attributes = True