from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class AgentType(str, Enum):

    MARKET = "market"

    TECHNICAL = "technical"

    FUNDAMENTAL = "fundamental"

    NEWS = "news"

    RISK = "risk"

    PORTFOLIO = "portfolio"

    MEMORY = "memory"

    MACRO = "macro"

    PREDICTION = "prediction"

    EXPLAIN = "explain"

    VISION = "vision"


@dataclass
class AITask:

    agent: AgentType

    priority: int = 1

    required: bool = True