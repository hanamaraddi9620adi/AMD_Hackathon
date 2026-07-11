from __future__ import annotations

import pandas as pd

from app.indicators.moving_average import moving_average_engine
from app.indicators.momentum import momentum_engine
from app.indicators.volatility import volatility_engine
from app.indicators.volume import volume_engine

from app.scoring.technical_score import technical_scorer


class TechnicalAgent:
    """
    Technical Analysis Agent
    """

    def analyze(
        self,
        market: dict,
    ) -> dict:

        history = market.get("history", [])

        if len(history) < 50:
            return {
                "technical_score": 50,
                "trend": "Neutral",
                "reasons": ["Not enough historical data"],
                "rsi": None,
                "macd": None,
                "ema20": None,
                "ema50": None,
                "ema200": None,
                "adx": None,
                "atr": None,
                "vwap": None,
                "volume_ratio": None,
            }

        try:

            df = pd.DataFrame(history)

            df.columns = [c.lower() for c in df.columns]

            df = moving_average_engine.calculate(df)
            df = momentum_engine.calculate(df)
            df = volatility_engine.calculate(df)
            df = volume_engine.calculate(df)

            technical = technical_scorer.calculate(df)

            latest = df.iloc[-1]

            return {

                "technical_score": technical["technical_score"],

                "trend": technical["trend"],

                "reasons": technical["reasons"],

                "rsi": float(latest["rsi"]) if pd.notna(latest["rsi"]) else None,

                "macd": float(latest["macd"]) if pd.notna(latest["macd"]) else None,

                "ema20": float(latest["ema20"]) if pd.notna(latest["ema20"]) else None,

                "ema50": float(latest["ema50"]) if pd.notna(latest["ema50"]) else None,

                "ema200": float(latest["ema200"]) if pd.notna(latest["ema200"]) else None,

                "adx": float(latest["adx"]) if pd.notna(latest["adx"]) else None,

                "atr": float(latest["atr"]) if pd.notna(latest["atr"]) else None,

                "vwap": float(latest["vwap"]) if pd.notna(latest["vwap"]) else None,

                "volume_ratio": float(latest["volume_ratio"]) if pd.notna(latest["volume_ratio"]) else None,
            }

        except Exception as e:

            return {

                "technical_score": 50,

                "trend": "Neutral",

                "reasons": [f"Technical analysis unavailable: {str(e)}"],

                "rsi": None,

                "macd": None,

                "ema20": None,

                "ema50": None,

                "ema200": None,

                "adx": None,

                "atr": None,

                "vwap": None,

                "volume_ratio": None,
            }


technical_agent = TechnicalAgent()