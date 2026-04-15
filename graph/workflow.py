from langgraph.graph import StateGraph, END
from graph.state import BIState
from graph.nodes import (
    # Layer 1
    manager_node,
    # Layer 2
    research_supervisor_node,
    analysis_supervisor_node,
    writer_supervisor_node,
    # Layer 3 - Research Workers
    web_search_worker_node,
    news_worker_node,
    # Layer 3 - Analysis Workers
    financial_worker_node,
    competitor_worker_node,
    # Layer 3 - Writing Workers
    report_writer_node,
    executive_summary_node,
)


def build_graph():
    """
    3-Layer Multi-Agent Business Intelligence Graph

    Layer 1 — Manager
        manager

    Layer 2 — Supervisors (3)
        research_supervisor → analysis_supervisor → writer_supervisor

    Layer 3 — Workers (6)
        web_search_worker + news_worker
        financial_worker  + competitor_worker
        report_writer     + executive_summary

    Flow:
        manager
          → research_supervisor
            → web_search_worker
            → news_worker
          → analysis_supervisor
            → financial_worker
            → competitor_worker
          → writer_supervisor
            → report_writer
            → executive_summary
          → END
    """
    graph = StateGraph(BIState)

    # ── Register all 10 nodes ─────────────────────────────
    # Layer 1
    graph.add_node("manager",               manager_node)

    # Layer 2 — Supervisors
    graph.add_node("research_supervisor",   research_supervisor_node)
    graph.add_node("analysis_supervisor",   analysis_supervisor_node)
    graph.add_node("writer_supervisor",     writer_supervisor_node)

    # Layer 3 — Research Workers
    graph.add_node("web_search_worker",     web_search_worker_node)
    graph.add_node("news_worker",           news_worker_node)

    # Layer 3 — Analysis Workers
    graph.add_node("financial_worker",      financial_worker_node)
    graph.add_node("competitor_worker",     competitor_worker_node)

    # Layer 3 — Writing Workers
    graph.add_node("report_writer",         report_writer_node)
    graph.add_node("executive_summary",     executive_summary_node)

    # ── Define edges (the orchestration flow) ─────────────
    graph.set_entry_point("manager")

    # Manager → Research Supervisor
    graph.add_edge("manager",              "research_supervisor")

    # Research Supervisor → its 2 workers (sequential)
    graph.add_edge("research_supervisor",  "web_search_worker")
    graph.add_edge("web_search_worker",    "news_worker")

    # Research done → Analysis Supervisor
    graph.add_edge("news_worker",          "analysis_supervisor")

    # Analysis Supervisor → its 2 workers (sequential)
    graph.add_edge("analysis_supervisor",  "financial_worker")
    graph.add_edge("financial_worker",     "competitor_worker")

    # Analysis done → Writer Supervisor
    graph.add_edge("competitor_worker",    "writer_supervisor")

    # Writer Supervisor → its 2 workers (sequential)
    graph.add_edge("writer_supervisor",    "report_writer")
    graph.add_edge("report_writer",        "executive_summary")

    # All done
    graph.add_edge("executive_summary",    END)

    return graph.compile()
