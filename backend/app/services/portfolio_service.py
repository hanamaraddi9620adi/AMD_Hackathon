from sqlalchemy.orm import Session

from app.models.portfolio import Portfolio
from app.models.user import User
from app.repositories.portfolio_repository import (
    portfolio_repository,
)


class PortfolioService:
    """
    Business Logic Layer for Portfolio.
    """

    def create_portfolio(
        self,
        db: Session,
        current_user: User,
        symbol: str,
        exchange: str,
        quantity: int,
        average_price: float,
        sector: str,
        notes: str,
    ) -> Portfolio:

        existing = portfolio_repository.get_by_symbol(
            db=db,
            user_id=current_user.id,
            symbol=symbol,
        )

        if existing:
            raise ValueError(
                f"{symbol.upper()} already exists in your portfolio."
            )

        portfolio = Portfolio(
            user_id=current_user.id,
            symbol=symbol.upper(),
            exchange=exchange.upper(),
            quantity=quantity,
            average_price=average_price,
            sector=sector,
            notes=notes,
        )

        return portfolio_repository.create(
            db=db,
            portfolio=portfolio,
        )

    def get_portfolio(
        self,
        db: Session,
        current_user: User,
    ) -> list[Portfolio]:

        return portfolio_repository.get_all_by_user(
            db=db,
            user_id=current_user.id,
        )

    def update_portfolio(
        self,
        db: Session,
        current_user: User,
        portfolio_id: str,
        quantity: int,
        average_price: float,
        sector: str,
        notes: str,
    ) -> Portfolio:

        portfolio = portfolio_repository.get_by_id(
            db=db,
            portfolio_id=portfolio_id,
        )

        if portfolio is None:
            raise ValueError(
                "Portfolio holding not found."
            )

        if portfolio.user_id != current_user.id:
            raise ValueError(
                "Unauthorized portfolio access."
            )

        portfolio.quantity = quantity
        portfolio.average_price = average_price
        portfolio.sector = sector
        portfolio.notes = notes

        return portfolio_repository.update(
            db=db,
            portfolio=portfolio,
        )

    def delete_portfolio(
        self,
        db: Session,
        current_user: User,
        portfolio_id: str,
    ):

        portfolio = portfolio_repository.get_by_id(
            db=db,
            portfolio_id=portfolio_id,
        )

        if portfolio is None:
            raise ValueError(
                "Portfolio holding not found."
            )

        if portfolio.user_id != current_user.id:
            raise ValueError(
                "Unauthorized portfolio access."
            )

        portfolio_repository.delete(
            db=db,
            portfolio=portfolio,
        )

        return {
            "message": "Portfolio holding deleted successfully."
        }


portfolio_service = PortfolioService()