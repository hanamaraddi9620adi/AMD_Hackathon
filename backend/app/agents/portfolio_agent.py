from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.portfolio_repository import (
    portfolio_repository,
)


class PortfolioAgent:
    """
    Portfolio Analysis Agent
    """

    def analyze(
        self,
        db: Session,
        current_user: User,
    ):

        portfolio = portfolio_repository.get_all_by_user(
            db,
            current_user.id,
        )

        total_stocks = len(portfolio)

        total_quantity = sum(
            stock.quantity
            for stock in portfolio
        )

        total_investment = sum(
            stock.quantity * stock.average_price
            for stock in portfolio
        )

        diversification = (
            "Good"
            if total_stocks >= 5
            else "Needs Improvement"
        )

        return {
            "total_holdings": total_stocks,
            "total_quantity": total_quantity,
            "total_investment": round(
                total_investment,
                2,
            ),
            "diversification": diversification,
            "holdings": portfolio,
        }


portfolio_agent = PortfolioAgent()