from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TechnicalAnalysis:

    trend: str = "Unknown"

    market_strength: float = 0.0

    momentum: float = 0.0

    volatility: float = 0.0

    support: float = 0.0

    resistance: float = 0.0

    rsi: float = 0.0

    macd: float = 0.0

    ema20: float = 0.0

    ema50: float = 0.0

    ema200: float = 0.0

    atr: float = 0.0

    adx: float = 0.0

    volume_score: float = 0.0

    score: float = 0.0


@dataclass
class FundamentalAnalysis:

    pe_ratio: float = 0.0

    eps: float = 0.0

    market_cap: float = 0.0

    beta: float = 0.0

    dividend_yield: float = 0.0

    score: float = 0.0


@dataclass
class NewsAnalysis:

    sentiment: str = "Neutral"

    sentiment_score: float = 0.0

    headline_count: int = 0

    summary: str = ""

    sources: list[str] = field(
        default_factory=list
    )


@dataclass
class RiskAnalysis:

    volatility: str = "Medium"

    risk_score: float = 0.0

    max_drawdown: float = 0.0

    confidence: float = 0.0