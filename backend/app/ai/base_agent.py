from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.models_ai.research_report import ResearchReport


class BaseAgent(ABC):
    """
    Base class for every AI Agent.

    Every agent must implement execute().

    The orchestrator only communicates
    with BaseAgent.

    This makes every agent interchangeable.
    """

    name: str = "BaseAgent"

    @abstractmethod
    async def execute(
        self,
        report: ResearchReport,
        context: dict,
    ) -> ResearchReport:
        """
        Executes the agent.

        Parameters
        ----------
        report

            Shared AI Research Report

        context

            Shared runtime context

        Returns
        -------

        Updated Research Report
        """

        raise NotImplementedError