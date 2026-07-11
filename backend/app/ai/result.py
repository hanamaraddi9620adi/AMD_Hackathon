from dataclasses import dataclass


@dataclass
class AgentResult:
    """
    Execution metadata.
    """

    agent: str

    success: bool

    execution_time: float

    message: str = ""