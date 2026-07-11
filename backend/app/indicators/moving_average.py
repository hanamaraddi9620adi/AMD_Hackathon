from __future__ import annotations

import logging

import pandas as pd

from ta.trend import EMAIndicator
from ta.trend import SMAIndicator

from app.indicators.base import (
    IndicatorEngine,
)

logger = logging.getLogger(__name__)


class MovingAverageEngine(IndicatorEngine):
    """
    Production-grade Moving Average Engine.

    Computes:

    • SMA20
    • SMA50
    • SMA100
    • SMA200

    • EMA20
    • EMA50
    • EMA100
    • EMA200

    """

    @staticmethod
    def calculate(
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = IndicatorEngine.prepare(df)

        close = df["close"]

        # -----------------------------
        # Simple Moving Averages
        # -----------------------------

        df["sma20"] = SMAIndicator(
            close,
            window=20,
        ).sma_indicator()

        df["sma50"] = SMAIndicator(
            close,
            window=50,
        ).sma_indicator()

        df["sma100"] = SMAIndicator(
            close,
            window=100,
        ).sma_indicator()

        df["sma200"] = SMAIndicator(
            close,
            window=200,
        ).sma_indicator()

        # -----------------------------
        # Exponential Moving Averages
        # -----------------------------

        df["ema20"] = EMAIndicator(
            close,
            window=20,
        ).ema_indicator()

        df["ema50"] = EMAIndicator(
            close,
            window=50,
        ).ema_indicator()

        df["ema100"] = EMAIndicator(
            close,
            window=100,
        ).ema_indicator()

        df["ema200"] = EMAIndicator(
            close,
            window=200,
        ).ema_indicator()

        logger.info(
            "Moving averages calculated successfully."
        )

        return df


moving_average_engine = MovingAverageEngine()