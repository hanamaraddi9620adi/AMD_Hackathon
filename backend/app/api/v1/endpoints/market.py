from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.market_schema import (
    MarketAnalysisResponse,
)

from app.services.market_service import (
    market_service,
)

router = APIRouter(
    prefix="/market",
    tags=["Market"],
)


@router.get(
    "/analyze/{symbol}",
    response_model=MarketAnalysisResponse,
)
def analyze_stock(
    symbol: str,
):
    """
    Analyze any stock symbol.
    Example:
    INFY
    TCS
    RELIANCE
    HDFCBANK
    """

    try:

        return market_service.analyze_stock(
            symbol,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )