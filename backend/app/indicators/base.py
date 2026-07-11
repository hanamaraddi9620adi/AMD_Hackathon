from __future__ import annotations

import logging

import pandas as pd


logger = logging.getLogger(__name__)


class IndicatorError(Exception):
    """Raised when an indicator cannot be calculated."""


class IndicatorEngine:
    """
    Base class shared by all indicator modules.

    Responsibilities:
    - Validate market dataframe
    - Handle missing values
    - Provide reusable helpers
    """

    REQUIRED_COLUMNS = [
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    @staticmethod
    def validate(df: pd.DataFrame) -> None:
        """
        Validate that the dataframe contains
        all required OHLCV columns.
        """

        if df.empty:
            raise IndicatorError("Market dataframe is empty.")

        missing = [
            column
            for column in IndicatorEngine.REQUIRED_COLUMNS
            if column not in df.columns
        ]

        if missing:
            raise IndicatorError(
                f"Missing required columns: {missing}"
            )

    @staticmethod
    def prepare(df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean market dataframe before indicators
        are calculated.
        """

        IndicatorEngine.validate(df)

        cleaned = df.copy()

        cleaned = cleaned.dropna()

        cleaned.reset_index(
            drop=True,
            inplace=True,
        )

        return cleaned