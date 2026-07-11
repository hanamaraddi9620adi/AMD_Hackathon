from app.agents.market_agent import market_agent


class FundamentalAgent:
    """
    Fundamental Analysis Agent.
    """

    def analyze(
        self,
        symbol: str,
    ) -> dict:

        market = market_agent.analyze(symbol)

        score = 50
        reasons = []

        pe = market.get("pe_ratio")
        beta = market.get("beta")
        market_cap = market.get("market_cap")
        eps = market.get("eps")
        dividend = market.get("dividend_yield")

        if pe is not None:
            if 10 <= pe <= 30:
                score += 15
                reasons.append("Healthy PE Ratio")
            elif pe > 50:
                score -= 10
                reasons.append("High PE Ratio")

        if eps is not None and eps > 0:
            score += 15
            reasons.append("Positive EPS")

        if beta is not None:
            if beta < 1.2:
                score += 10
                reasons.append("Stable Beta")
            else:
                score -= 5
                reasons.append("High Beta")

        if market_cap is not None and market_cap > 1_000_000_000:
            score += 10
            reasons.append("Large Market Cap")

        if dividend:
            score += 5
            reasons.append("Dividend Paying Company")

        score = max(0, min(score, 100))

        return {
            "fundamental_score": score,
            "pe_ratio": pe,
            "eps": eps,
            "beta": beta,
            "market_cap": market_cap,
            "dividend_yield": dividend,
            "reasons": reasons,
        }


fundamental_agent = FundamentalAgent()