from sqlalchemy.orm import Session

from app.models.user import User

from app.agents.market_agent import market_agent
from app.agents.technical_agent import technical_agent
from app.agents.news_agent import news_agent
from app.agents.sentiment_agent import sentiment_agent
from app.agents.risk_agent import risk_agent
from app.agents.portfolio_agent import portfolio_agent
from app.agents.explainability_agent import explainability_agent


class Orchestrator:
    """
    Central AI Decision Engine
    """

    def analyze(
        self,
        db: Session,
        current_user: User,
        symbol: str,
    ):

        market = market_agent.analyze(symbol)

        technical = technical_agent.analyze(symbol)

        news = news_agent.analyze(symbol)

        sentiment = sentiment_agent.analyze(symbol)

        risk = risk_agent.analyze(symbol)

        portfolio = portfolio_agent.analyze(
            db,
            current_user,
        )

        explanation = explainability_agent.explain(
            recommendation=sentiment["recommendation"],
            technical=technical,
            sentiment=sentiment,
            risk=risk,
        )

        return {
            "market": market,
            "technical": technical,
            "news": news,
            "sentiment": sentiment,
            "risk": risk,
            "portfolio": portfolio,
            "analysis": explanation,
        }


orchestrator = Orchestrator()