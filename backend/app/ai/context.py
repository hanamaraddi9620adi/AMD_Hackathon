from dataclasses import dataclass
from dataclasses import field


@dataclass
class AIContext:
    """
    Shared execution context
    between all AI agents.
    """

    query: str

    symbol: str | None = None

    user_id: str | None = None

    metadata: dict = field(
        default_factory=dict
    )