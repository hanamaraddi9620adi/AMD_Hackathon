class ExplainabilityAgent:
    """
    Converts AI outputs into a human-readable explanation.
    """

    def explain(
        self,
        recommendation: str,
        technical: dict,
        sentiment: dict,
        risk: dict,
    ):

        reasons = []

        reasons.append(
            f"Technical Trend: {technical['trend']}"
        )

        reasons.append(
            f"Market Sentiment: {sentiment['sentiment']}"
        )

        reasons.append(
            f"Risk Level: {risk['risk_level']}"
        )

        reasons.append(
            f"Confidence Score: {sentiment['confidence']}%"
        )

        if recommendation == "BUY":
            summary = (
                "The stock shows strong technical momentum "
                "with positive sentiment and acceptable risk."
            )

        elif recommendation == "HOLD":
            summary = (
                "Signals are mixed. Waiting for confirmation "
                "is recommended."
            )

        else:
            summary = (
                "Current market conditions are unfavorable."
            )

        return {
            "recommendation": recommendation,
            "summary": summary,
            "reasons": reasons,
        }


explainability_agent = ExplainabilityAgent()