import os
import json
from groq import Groq
from dotenv import load_dotenv
from tools.search_tool import search_web

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL  = "llama-3.3-70b-versatile"


def llm(system: str, user: str, temperature: float = 0.7) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system",  "content": system},
            {"role": "user",    "content": user}
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def manager_node(state: dict) -> dict:
    company = state["company"]

    plan = llm(
        system=(
            "You are a senior Business Intelligence Manager. "
            "Your job is to create a detailed research and analysis plan for a company. "
            "The plan must cover: what to research online, what news to find, "
            "what financial data to analyze, who the competitors are, and how to write the final report. "
            "Be specific and professional. Write in clear bullet points per section."
        ),
        user=(
            f"Company / Topic: {company}\n\n"
            "Create a full BI research plan covering:\n"
            "1. Research goals (what to search online)\n"
            "2. News focus (what recent news to find)\n"
            "3. Financial analysis goals\n"
            "4. Competitor analysis goals\n"
            "5. Report writing guidelines"
        )
    )

    return {"research_plan": plan}


def research_supervisor_node(state: dict) -> dict:
    company = state["company"]
    plan    = state["research_plan"]

    raw = llm(
        system=(
            "You are a Research Supervisor managing two workers: "
            "a Web Search Worker and a News Worker. "
            "Based on the manager's plan, generate exactly 2 search queries: "
            "one for general web research and one for recent news. "
            "Return ONLY a valid JSON array of exactly 2 strings. No explanation."
        ),
        user=f"Company: {company}\n\nManager's Plan:\n{plan}\n\nGenerate 2 search queries."
    )

    raw = raw.strip().strip("```json").strip("```").strip()
    try:
        tasks = json.loads(raw)
        if not isinstance(tasks, list) or len(tasks) < 2:
            tasks = [f"{company} business overview", f"{company} latest news 2025"]
    except Exception:
        tasks = [f"{company} business overview", f"{company} latest news 2025"]

    return {"research_tasks": tasks}


def web_search_worker_node(state: dict) -> dict:
    query   = state["research_tasks"][0]
    results = search_web(query, max_results=3)

    summary = llm(
        system="You are a research analyst. Summarize the web search results into clean, structured bullet points.",
        user=f"Query: {query}\n\nRaw Results:\n{results}\n\nProvide a structured summary."
    )

    return {"web_research": summary}


def news_worker_node(state: dict) -> dict:
    query   = state["research_tasks"][1]
    results = search_web(query, max_results=3)

    summary = llm(
        system="You are a news analyst. Summarize the latest news results into key headlines and insights.",
        user=f"Query: {query}\n\nRaw News Results:\n{results}\n\nProvide a news summary with key takeaways."
    )

    return {"news_research": summary}


def analysis_supervisor_node(state: dict) -> dict:
    company      = state["company"]
    web_research = state["web_research"]

    raw = llm(
        system=(
            "You are an Analysis Supervisor managing two workers: "
            "a Financial Analysis Worker and a Competitor Analysis Worker. "
            "Based on the company and research, generate 2 specific search queries: "
            "one for financial data/metrics and one for competitors. "
            "Return ONLY a valid JSON array of exactly 2 strings. No explanation."
        ),
        user=(
            f"Company: {company}\n\n"
            f"Research Summary:\n{web_research[:500]}\n\n"
            "Generate 2 analysis queries."
        )
    )

    raw = raw.strip().strip("```json").strip("```").strip()
    try:
        tasks = json.loads(raw)
        if not isinstance(tasks, list) or len(tasks) < 2:
            tasks = [f"{company} financial performance revenue", f"{company} top competitors market"]
    except Exception:
        tasks = [f"{company} financial performance revenue", f"{company} top competitors market"]

    return {"analysis_tasks": tasks}


def financial_worker_node(state: dict) -> dict:
    query   = state["analysis_tasks"][0]
    results = search_web(query, max_results=3)

    analysis = llm(
        system=(
            "You are a financial analyst. Analyze the data and produce a structured financial analysis "
            "including: revenue trends, growth indicators, market position, and financial health signals. "
            "Use bullet points and be concise."
        ),
        user=f"Query: {query}\n\nRaw Data:\n{results}\n\nProvide financial analysis."
    )

    return {"financial_analysis": analysis}


def competitor_worker_node(state: dict) -> dict:
    query   = state["analysis_tasks"][1]
    results = search_web(query, max_results=3)

    analysis = llm(
        system=(
            "You are a competitive intelligence analyst. Identify key competitors and analyze "
            "their strengths, weaknesses, and market positioning compared to the company. "
            "Use bullet points. Be concise and factual."
        ),
        user=f"Query: {query}\n\nRaw Data:\n{results}\n\nProvide competitor analysis."
    )

    return {"competitor_analysis": analysis}


def writer_supervisor_node(state: dict) -> dict:
    company = state["company"]

    tasks = [
        f"Write a full detailed business intelligence report for {company} covering all research and analysis",
        f"Write a concise executive summary for {company} with key insights and recommendations"
    ]

    return {"writing_tasks": tasks}


def report_writer_node(state: dict) -> dict:
    company  = state["company"]
    sections = {
        "Web Research":          state.get("web_research", ""),
        "News":                  state.get("news_research", ""),
        "Financial Analysis":    state.get("financial_analysis", ""),
        "Competitor Analysis":   state.get("competitor_analysis", ""),
    }

    combined = "\n\n".join(
        f"### {title}\n{content}" for title, content in sections.items()
    )

    report = llm(
        system=(
            "You are a senior business report writer. "
            "Using all the research and analysis data provided, write a comprehensive, "
            "professional Business Intelligence Report in Markdown format. "
            "Include these sections: Overview, Market Position, Recent News, "
            "Financial Health, Competitive Landscape, Key Risks, Opportunities. "
            "Be detailed, structured, and professional."
        ),
        user=f"Company: {company}\n\nAll Research & Analysis Data:\n{combined}\n\nWrite the full BI report."
    )

    return {"full_report": report}


def executive_summary_node(state: dict) -> dict:
    company     = state["company"]
    full_report = state["full_report"]

    summary = llm(
        system=(
            "You are a C-suite communication specialist. "
            "Write a sharp, concise Executive Summary (max 300 words) from the full report. "
            "It must include: 3 key insights, 2 main risks, and 2 strategic recommendations. "
            "Format in Markdown. Write for a busy CEO."
        ),
        user=f"Company: {company}\n\nFull Report:\n{full_report}\n\nWrite the executive summary."
    )

    return {"executive_summary": summary}
