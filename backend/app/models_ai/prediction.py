from dataclasses import dataclass
from dataclasses import field


@dataclass
class MarketScenario:

    probability: float

    description: str

    target_price: float

    conditions: list[str] = field(
        default_factory=list
    )


@dataclass
class Prediction:

    bullish: MarketScenario

    neutral: MarketScenario

    bearish: MarketScenario

    confidence: float