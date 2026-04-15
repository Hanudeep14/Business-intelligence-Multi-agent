from langgraph.graph import StateGraph, END
from graph.state import BIState
from graph.nodes import (
    manager_node,
    research_supervisor_node,
    analysis_supervisor_node,
    writer_supervisor_node,
    web_search_worker_node,
    news_worker_node,
    financial_worker_node,
    competitor_worker_node,
    report_writer_node,
    executive_summary_node,
)


def build_graph():
    graph = StateGraph(BIState)

    graph.add_node("manager",               manager_node)
    graph.add_node("research_supervisor",   research_supervisor_node)
    graph.add_node("analysis_supervisor",   analysis_supervisor_node)
    graph.add_node("writer_supervisor",     writer_supervisor_node)
    graph.add_node("web_search_worker",     web_search_worker_node)
    graph.add_node("news_worker",           news_worker_node)
    graph.add_node("financial_worker",      financial_worker_node)
    graph.add_node("competitor_worker",     competitor_worker_node)
    graph.add_node("report_writer",         report_writer_node)
    graph.add_node("executive_summary",     executive_summary_node)

    graph.set_entry_point("manager")

    graph.add_edge("manager",              "research_supervisor")
    graph.add_edge("research_supervisor",  "web_search_worker")
    graph.add_edge("web_search_worker",    "news_worker")
    graph.add_edge("news_worker",          "analysis_supervisor")
    graph.add_edge("analysis_supervisor",  "financial_worker")
    graph.add_edge("financial_worker",     "competitor_worker")
    graph.add_edge("competitor_worker",    "writer_supervisor")
    graph.add_edge("writer_supervisor",    "report_writer")
    graph.add_edge("report_writer",        "executive_summary")
    graph.add_edge("executive_summary",    END)

    return graph.compile()
