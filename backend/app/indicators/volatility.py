from __future__ import annotations

import logging

import pandas as pd

from ta.volatility import AverageTrueRange
from ta.volatility import BollingerBands

from ta.trend import ADXIndicator

from app.indicators.base import IndicatorEngine

logger = logging.getLogger(__name__)


class VolatilityEngine(IndicatorEngine):
    """
    Volatility Indicator Engine

    Computes

    • ATR

    • Bollinger Bands

    • ADX

    • Standard Deviation

    """

    @staticmethod
    def calculate(
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = IndicatorEngine.prepare(df)

        close = df["close"]
        high = df["high"]
        low = df["low"]

        # ------------------------
        # ATR
        # ------------------------

        atr = AverageTrueRange(
            high=high,
            low=low,
            close=close,
            window=14,
        )

        df["atr"] = atr.average_true_range()

        # ------------------------
        # ADX
        # ------------------------

        adx = ADXIndicator(
            high=high,
            low=low,
            close=close,
            window=14,
        )

        df["adx"] = adx.adx()

        df["adx_positive"] = adx.adx_pos()

        df["adx_negative"] = adx.adx_neg()

        # ------------------------
        # Bollinger Bands
        # ------------------------

        bb = BollingerBands(
            close=close,
            window=20,
            window_dev=2,
        )

        df["bb_upper"] = bb.bollinger_hband()

        df["bb_middle"] = bb.bollinger_mavg()

        df["bb_lower"] = bb.bollinger_lband()

        df["bb_width"] = (
            df["bb_upper"] - df["bb_lower"]
        )

        # ------------------------
        # Standard Deviation
        # ------------------------

        df["std_dev"] = close.rolling(
            window=20,
        ).std()

        logger.info(
            "Volatility indicators calculated successfully."
        )

        return df


volatility_engine = VolatilityEngine()