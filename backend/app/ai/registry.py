from app.ai.task import AgentType


class AgentRegistry:
    """
    Stores every AI Agent.

    Planner only knows AgentType.

    Registry returns the implementation.
    """

    def __init__(self):

        self._agents = {}

    def register(
        self,
        agent_type: AgentType,
        agent,
    ):

        self._agents[agent_type] = agent

    def get(
        self,
        agent_type: AgentType,
    ):

        return self._agents[agent_type]


registry = AgentRegistry()