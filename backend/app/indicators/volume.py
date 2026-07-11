from __future__ import annotations

import logging

import pandas as pd

from ta.volume import (
    OnBalanceVolumeIndicator,
    VolumeWeightedAveragePrice,
    ChaikinMoneyFlowIndicator,
)

from app.indicators.base import IndicatorEngine

logger = logging.getLogger(__name__)


class VolumeEngine(IndicatorEngine):
    """
    Volume Analysis Engine
    """

    @staticmethod
    def calculate(
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = IndicatorEngine.prepare(df)

        close = df["close"]
        high = df["high"]
        low = df["low"]
        volume = df["volume"]

        # --------------------------
        # OBV
        # --------------------------

        obv = OnBalanceVolumeIndicator(
            close=close,
            volume=volume,
        )

        df["obv"] = obv.on_balance_volume()

        # --------------------------
        # VWAP
        # --------------------------

        vwap = VolumeWeightedAveragePrice(
            high=high,
            low=low,
            close=close,
            volume=volume,
        )

        df["vwap"] = (
            vwap.volume_weighted_average_price()
        )

        # --------------------------
        # CMF
        # --------------------------

        cmf = ChaikinMoneyFlowIndicator(
            high=high,
            low=low,
            close=close,
            volume=volume,
            window=20,
        )

        df["cmf"] = cmf.chaikin_money_flow()

        # --------------------------
        # Volume Trend
        # --------------------------

        df["volume_sma20"] = (
            volume.rolling(20).mean()
        )

        df["volume_ratio"] = (
            volume / df["volume_sma20"]
        )

        logger.info(
            "Volume indicators calculated."
        )

        return df


volume_engine = VolumeEngine()