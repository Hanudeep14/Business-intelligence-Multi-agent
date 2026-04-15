from typing import TypedDict, List


class BIState(TypedDict):
    # ── Layer 0: User Input
    company: str                  # Company or topic to research

    # ── Layer 1: Manager
    research_plan: str            # Manager's plan for supervisors

    # ── Layer 2a: Research Supervisor
    research_tasks: List[str]     # Tasks assigned to research workers

    # ── Layer 3a: Research Workers
    web_research: str             # Web Search Worker output
    news_research: str            # News Worker output

    # ── Layer 2b: Analysis Supervisor
    analysis_tasks: List[str]     # Tasks assigned to analysis workers

    # ── Layer 3b: Analysis Workers
    financial_analysis: str       # Financial Analysis Worker output
    competitor_analysis: str      # Competitor Analysis Worker output

    # ── Layer 2c: Writer Supervisor
    writing_tasks: List[str]      # Tasks assigned to writing workers

    # ── Layer 3c: Writing Workers
    full_report: str              # Full Detailed Report Worker output
    executive_summary: str        # Executive Summary Worker output
