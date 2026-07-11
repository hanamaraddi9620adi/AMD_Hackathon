from pydantic import BaseModel, Field


class PortfolioCreate(BaseModel):

    symbol: str = Field(
        ...,
        min_length=1,
        max_length=20,
    )

    exchange: str = Field(
        default="NSE",
        max_length=20,
    )

    quantity: int = Field(
        ...,
        gt=0,
    )

    average_price: float = Field(
        ...,
        gt=0,
    )

    sector: str = Field(
        default="Unknown",
        max_length=100,
    )

    notes: str = Field(
        default="",
        max_length=500,
    )


class PortfolioUpdate(BaseModel):

    quantity: int | None = Field(
        default=None,
        gt=0,
    )

    average_price: float | None = Field(
        default=None,
        gt=0,
    )

    sector: str | None = Field(
        default=None,
        max_length=100,
    )

    notes: str | None = Field(
        default=None,
        max_length=500,
    )


class PortfolioResponse(BaseModel):

    id: str

    symbol: str

    exchange: str

    quantity: int

    average_price: float

    sector: str

    notes: str

    class Config:
        from_attributes = True