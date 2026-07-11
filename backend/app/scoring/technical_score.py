from __future__ import annotations

import pandas as pd


class TechnicalScorer:
    """
    Calculates an overall technical score (0-100)
    from the latest indicator values.
    """

    def calculate(self, df: pd.DataFrame) -> dict:

        latest = df.iloc[-1]

        score = 0
        reasons = []

        # EMA Trend
        if latest["ema20"] > latest["ema50"]:
            score += 15
            reasons.append("EMA20 above EMA50")

        if latest["ema50"] > latest["ema200"]:
            score += 15
            reasons.append("EMA50 above EMA200")

        # RSI
        if 45 <= latest["rsi"] <= 65:
            score += 15
            reasons.append("Healthy RSI")

        elif latest["rsi"] < 30:
            score += 10
            reasons.append("Oversold")

        elif latest["rsi"] > 70:
            score -= 5
            reasons.append("Overbought")

        # MACD
        if latest["macd"] > latest["macd_signal"]:
            score += 15
            reasons.append("Bullish MACD crossover")

        # ADX
        if latest["adx"] > 25:
            score += 10
            reasons.append("Strong trend")

        # VWAP
        if latest["close"] > latest["vwap"]:
            score += 10
            reasons.append("Trading above VWAP")

        # Volume
        if latest["volume_ratio"] > 1:
            score += 10
            reasons.append("Above average volume")

        score = max(0, min(score, 100))

        if score >= 80:
            trend = "Strong Bullish"
        elif score >= 65:
            trend = "Bullish"
        elif score >= 45:
            trend = "Neutral"
        elif score >= 25:
            trend = "Bearish"
        else:
            trend = "Strong Bearish"

        return {
            "technical_score": score,
            "trend": trend,
            "reasons": reasons,
        }


technical_scorer = TechnicalScorer()