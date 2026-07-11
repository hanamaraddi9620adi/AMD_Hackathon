from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from app.ai.task import AITask


@dataclass
class ExecutionPlan:

    symbol: str | None = None

    tasks: list[AITask] = field(
        default_factory=list
    )

    user_intent: str = ""

    requires_market_data: bool = True