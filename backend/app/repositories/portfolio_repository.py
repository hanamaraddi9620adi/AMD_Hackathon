from sqlalchemy.orm import Session

from app.models.portfolio import Portfolio


class PortfolioRepository:
    """
    Repository layer responsible for all
    Portfolio database operations.
    """

    def create(
        self,
        db: Session,
        portfolio: Portfolio,
    ) -> Portfolio:

        db.add(portfolio)
        db.commit()
        db.refresh(portfolio)

        return portfolio

    def get_all_by_user(
        self,
        db: Session,
        user_id: str,
    ) -> list[Portfolio]:

        return (
            db.query(Portfolio)
            .filter(
                Portfolio.user_id == user_id,
                Portfolio.is_active == True,
            )
            .all()
        )

    def get_by_symbol(
        self,
        db: Session,
        user_id: str,
        symbol: str,
    ) -> Portfolio | None:

        return (
            db.query(Portfolio)
            .filter(
                Portfolio.user_id == user_id,
                Portfolio.symbol == symbol.upper(),
                Portfolio.is_active == True,
            )
            .first()
        )

    def get_by_id(
        self,
        db: Session,
        portfolio_id: str,
    ) -> Portfolio | None:

        return (
            db.query(Portfolio)
            .filter(
                Portfolio.id == portfolio_id,
                Portfolio.is_active == True,
            )
            .first()
        )

    def update(
        self,
        db: Session,
        portfolio: Portfolio,
    ) -> Portfolio:

        db.commit()
        db.refresh(portfolio)

        return portfolio

    def delete(
        self,
        db: Session,
        portfolio: Portfolio,
    ) -> None:

        portfolio.is_active = False

        db.commit()


portfolio_repository = PortfolioRepository()