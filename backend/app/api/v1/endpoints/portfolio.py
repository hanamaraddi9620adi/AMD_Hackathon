from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.sessions import get_db

from app.models.user import User

from app.schemas.portfolio_schema import (
    PortfolioCreate,
    PortfolioUpdate,
    PortfolioResponse,
)

from app.services.portfolio_service import (
    portfolio_service,
)

from app.api.deps import get_current_user


router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
)


@router.post(
    "/",
    response_model=PortfolioResponse,
)
def create_portfolio(
    request: PortfolioCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        return portfolio_service.create_portfolio(
            db=db,
            current_user=current_user,
            symbol=request.symbol,
            exchange=request.exchange,
            quantity=request.quantity,
            average_price=request.average_price,
            sector=request.sector,
            notes=request.notes,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[PortfolioResponse],
)
def get_portfolio(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return portfolio_service.get_portfolio(
        db=db,
        current_user=current_user,
    )


@router.put(
    "/{portfolio_id}",
    response_model=PortfolioResponse,
)
def update_portfolio(
    portfolio_id: str,
    request: PortfolioUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        return portfolio_service.update_portfolio(
            db=db,
            current_user=current_user,
            portfolio_id=portfolio_id,
            quantity=request.quantity,
            average_price=request.average_price,
            sector=request.sector,
            notes=request.notes,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete("/{portfolio_id}")
def delete_portfolio(
    portfolio_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        return portfolio_service.delete_portfolio(
            db=db,
            current_user=current_user,
            portfolio_id=portfolio_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )