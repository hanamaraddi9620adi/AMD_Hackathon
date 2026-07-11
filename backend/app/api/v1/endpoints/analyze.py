from fastapi import APIRouter
from fastapi import HTTPException

from app.services.analyze_service import (
    analyze_service,
)

router = APIRouter(
    prefix="/analyze",
    tags=["AI Analysis"],
)


@router.get("/{symbol}")
def analyze_stock(
    symbol: str,
):

    try:

        return analyze_service.analyze(
            symbol,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )