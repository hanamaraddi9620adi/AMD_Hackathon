from app.agents.news_agent import news_agent
from app.agents.technical_agent import technical_agent


class SentimentAgent:
    """
    Combines technical and news sentiment.
    """

    def analyze(
        self,
        symbol: str,
    ):

        technical = technical_agent.analyze(symbol)
        news = news_agent.analyze(symbol)

        score = (
            technical["confidence"] +
            news["confidence"]
        ) / 2

        if score >= 80:
            sentiment = "Bullish"
            recommendation = "BUY"

        elif score >= 60:
            sentiment = "Neutral"
            recommendation = "HOLD"

        else:
            sentiment = "Bearish"
            recommendation = "AVOID"

        return {
            "symbol": symbol.upper(),
            "sentiment": sentiment,
            "recommendation": recommendation,
            "confidence": round(score),
            "technical": technical,
            "news": news,
        }


sentiment_agent = SentimentAgent()