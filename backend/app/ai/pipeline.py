from app.ai.context import AIContext

from app.ai.plan import ExecutionPlan

from app.models_ai.research_report import (
    ResearchReport,
)


class AIPipeline:
    """
    Executes the AI Workflow.
    """

    async def execute(
        self,
        plan: ExecutionPlan,
        report: ResearchReport,
        context: AIContext,
    ) -> ResearchReport:

        raise NotImplementedError