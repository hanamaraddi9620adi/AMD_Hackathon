from pydantic import BaseModel


class MarketAnalysisResponse(BaseModel):
    """
    Response schema for market analysis.
    """

    symbol: str
    company_name: str
    exchange: str

    sector: str
    industry: str

    price: float
    previous_close: float
    change_percent: float

    open: float | None
    day_high: float | None
    day_low: float | None

    volume: int | None
    average_volume: int | None

    market_cap: int | None

    pe_ratio: float | None
    eps: float | None
    beta: float | None

    dividend_yield: float | None

    fifty_two_week_high: float | None
    fifty_two_week_low: float | None

    currency: str

    trend: str
    risk: str
    recommendation: str
    confidence: int

    history: list[float]

    class Config:
        from_attributes = True