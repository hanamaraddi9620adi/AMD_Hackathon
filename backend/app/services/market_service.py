from app.agents.market_agent import market_agent


class MarketService:
    """
    Business logic for live market analysis.

    This layer transforms raw market data
    into meaningful insights.
    """

    def analyze_stock(
        self,
        symbol: str,
    ) -> dict:

        data = market_agent.analyze(symbol)

        price = data["price"] or 0
        change = data["change_percent"] or 0

        # -------------------------
        # Trend
        # -------------------------

        if change > 2:
            trend = "Strong Bullish"

        elif change > 0:
            trend = "Bullish"

        elif change < -2:
            trend = "Strong Bearish"

        elif change < 0:
            trend = "Bearish"

        else:
            trend = "Sideways"

        # -------------------------
        # Risk Score
        # -------------------------

        beta = data.get("beta") or 1

        if beta >= 1.5:
            risk = "High"

        elif beta >= 1:
            risk = "Medium"

        else:
            risk = "Low"

        # -------------------------
        # Recommendation
        # -------------------------

        if trend.startswith("Strong Bullish") and risk != "High":
            recommendation = "Strong Buy"

        elif trend == "Bullish":
            recommendation = "Buy"

        elif trend == "Sideways":
            recommendation = "Hold"

        elif trend == "Bearish":
            recommendation = "Reduce"

        else:
            recommendation = "Sell"

        # -------------------------
        # Confidence Score
        # -------------------------

        confidence = 70

        if recommendation == "Strong Buy":
            confidence = 92

        elif recommendation == "Buy":
            confidence = 84

        elif recommendation == "Hold":
            confidence = 65

        elif recommendation == "Reduce":
            confidence = 58

        elif recommendation == "Sell":
            confidence = 90

        data["trend"] = trend
        data["risk"] = risk
        data["recommendation"] = recommendation
        data["confidence"] = confidence

        return data


market_service = MarketService()