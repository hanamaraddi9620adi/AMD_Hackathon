from dataclasses import dataclass
from dataclasses import field

from app.models_ai.analysis import (
    TechnicalAnalysis,
    FundamentalAnalysis,
    NewsAnalysis,
    RiskAnalysis,
)

from app.models_ai.prediction import Prediction


@dataclass
class ResearchReport:

    symbol: str

    company_name: str

    price: float

    exchange: str

    technical: TechnicalAnalysis

    fundamentals: FundamentalAnalysis

    news: NewsAnalysis

    risk: RiskAnalysis

    prediction: Prediction | None = None

    ai_summary: str = ""

    confidence: float = 0.0

    sources: list[str] = field(
        default_factory=list
    )