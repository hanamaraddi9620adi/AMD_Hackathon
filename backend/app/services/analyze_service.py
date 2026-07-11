from app.agents.market_agent import market_agent
from app.agents.technical_agent import technical_agent
from app.agents.fundamental_agent import fundamental_agent
from app.agents.risk_agent import risk_agent
from app.agents.news_agent import news_agent

from app.services.fireworks_service import fireworks_service


class AnalyzeService:

    def analyze(
        self,
        symbol: str,
    ) -> dict:

        market = market_agent.analyze(symbol)

        technical = technical_agent.analyze(market)

        fundamentals = fundamental_agent.analyze(symbol)

        risk = risk_agent.analyze(symbol)

        news = news_agent.analyze(symbol)

        summary = fireworks_service.generate_summary(
            symbol=symbol,
            market=market,
            technical=technical,
            fundamentals=fundamentals,
            news=news,
            risk=risk,
        )

        return {

            "symbol": symbol.upper(),

            "market": market,

            "technical": technical,

            "fundamentals": fundamentals,

            "risk": risk,

            "news": news,

            "summary": summary,
        }


analyze_service = AnalyzeService()