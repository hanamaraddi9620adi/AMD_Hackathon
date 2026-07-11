from app.agents.market_agent import market_agent


class RiskAgent:
    """
    AI Risk Analysis Agent.
    """

    def analyze(
        self,
        symbol: str,
    ) -> dict:

        market = market_agent.analyze(symbol)

        risk_score = 50

        risks = []

        beta = market.get("beta")
        change = abs(
            market.get("change_percent", 0)
        )

        market_cap = market.get("market_cap")

        if beta:

            if beta > 1.5:
                risk_score += 25
                risks.append("High Beta")

            elif beta < 1:
                risk_score -= 10
                risks.append("Stable Beta")

        if change > 4:
            risk_score += 20
            risks.append("High Daily Volatility")

        if market_cap:

            if market_cap < 5_000_000_000:
                risk_score += 10
                risks.append("Small Market Capitalization")

        risk_score = max(
            0,
            min(
                risk_score,
                100,
            ),
        )

        if risk_score < 35:
            level = "Low"

        elif risk_score < 70:
            level = "Medium"

        else:
            level = "High"

        return {

            "risk_score": risk_score,

            "risk_level": level,

            "beta": beta,

            "daily_change_percent": market.get(
                "change_percent"
            ),

            "risks": risks,
        }


risk_agent = RiskAgent()