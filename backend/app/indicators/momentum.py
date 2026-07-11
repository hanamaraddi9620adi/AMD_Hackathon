from __future__ import annotations

import logging

import pandas as pd

from ta.momentum import RSIIndicator
from ta.momentum import StochRSIIndicator
from ta.momentum import ROCIndicator
from ta.trend import MACD

from app.indicators.base import IndicatorEngine

logger = logging.getLogger(__name__)


class MomentumEngine(IndicatorEngine):
    """
    Momentum Indicator Engine.

    Calculates:

    • RSI (14)

    • MACD

    • MACD Signal

    • MACD Histogram

    • Rate of Change

    • Stochastic RSI

    """

    @staticmethod
    def calculate(
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = IndicatorEngine.prepare(df)

        close = df["close"]

        # -------------------------
        # RSI
        # -------------------------

        df["rsi"] = RSIIndicator(
            close=close,
            window=14,
        ).rsi()

        # -------------------------
        # MACD
        # -------------------------

        macd = MACD(
            close=close,
            window_fast=12,
            window_slow=26,
            window_sign=9,
        )

        df["macd"] = macd.macd()

        df["macd_signal"] = macd.macd_signal()

        df["macd_histogram"] = macd.macd_diff()

        # -------------------------
        # Rate of Change
        # -------------------------

        df["roc"] = ROCIndicator(
            close=close,
            window=12,
        ).roc()

        # -------------------------
        # Stochastic RSI
        # -------------------------

        stoch = StochRSIIndicator(
            close=close,
            window=14,
            smooth1=3,
            smooth2=3,
        )

        df["stoch_rsi"] = stoch.stochrsi()

        df["stoch_rsi_k"] = stoch.stochrsi_k()

        df["stoch_rsi_d"] = stoch.stochrsi_d()

        logger.info(
            "Momentum indicators calculated successfully."
        )

        return df


momentum_engine = MomentumEngine()