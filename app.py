import streamlit as st
from dotenv import load_dotenv
from graph.workflow import build_graph

load_dotenv()

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="BI Intelligence Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CSS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }

.hero-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 2.4rem; font-weight: 600;
    color: #f0b429;
    letter-spacing: -0.02em;
}
.hero-sub {
    color: #666; font-size: 0.9rem; margin-top: 4px; margin-bottom: 2rem;
}
.layer-header {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem; text-transform: uppercase;
    letter-spacing: 0.12em; color: #f0b429;
    margin-bottom: 6px; margin-top: 16px;
}
.agent-pill {
    display: inline-block;
    background: #1a1a1a; border: 1px solid #2a2a2a;
    border-radius: 20px; padding: 4px 12px;
    font-size: 0.78rem; color: #ccc;
    margin: 3px 2px;
}
.agent-pill.active { border-color: #f0b429; color: #f0b429; background: #1f1a00; }
.metric-card {
    background: #0f0f0f; border: 1px solid #222;
    border-radius: 10px; padding: 18px;
    text-align: center;
}
.metric-val {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 2rem; font-weight: 600; color: #f0b429;
}
.metric-lbl { color: #555; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 4px; }
.report-box {
    background: #0a0a0a; border: 1px solid #1e1e1e;
    border-radius: 10px; padding: 28px; line-height: 1.8;
}
.exec-box {
    background: #1a1200; border: 1px solid #f0b42933;
    border-radius: 10px; padding: 24px;
}
.tag {
    display: inline-block; background: #f0b42922;
    color: #f0b429; border-radius: 4px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem; padding: 2px 8px; margin-right: 6px;
}
.stButton > button {
    background: #f0b429; color: #000;
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 600; font-size: 0.85rem;
    border: none; border-radius: 8px;
    padding: 12px 28px; width: 100%;
    letter-spacing: 0.04em;
}
.stButton > button:hover { background: #ffc93c; transform: translateY(-1px); }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar — Architecture Map ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏗️ Agent Architecture")
    st.markdown("---")

    layers = [
        ("LAYER 1 — MANAGER", [("📋", "Manager", "Plans entire BI workflow")]),
        ("LAYER 2 — SUPERVISORS", [
            ("🔬", "Research Supervisor", "Delegates web + news tasks"),
            ("📈", "Analysis Supervisor", "Delegates finance + competitor tasks"),
            ("✍️", "Writer Supervisor",   "Delegates report + summary tasks"),
        ]),
        ("LAYER 3 — WORKERS", [
            ("🌐", "Web Search Worker",    "Live web research via Tavily"),
            ("📰", "News Worker",          "Latest news research"),
            ("💰", "Financial Worker",     "Revenue & financial metrics"),
            ("🏢", "Competitor Worker",    "Competitor intelligence"),
            ("📄", "Report Writer",        "Full BI report"),
            ("⚡", "Executive Summary",    "CEO-ready summary"),
        ]),
    ]

    for layer_name, agents in layers:
        st.markdown(f'<div class="layer-header">{layer_name}</div>', unsafe_allow_html=True)
        for icon, name, desc in agents:
            st.markdown(f"**{icon} {name}**")
            st.caption(desc)
        st.markdown("")

    st.markdown("---")
    st.markdown("**Stack**")
    st.code("LangGraph · 10 Agents\nGroq · Llama 3.3 70B\nTavily · Web Search\nStreamlit · UI", language="text")


# ─── Main UI ─────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">📊 Business Intelligence Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">3-Layer Multi-Agent Orchestration · Manager → Supervisors → Workers · Powered by LangGraph</div>', unsafe_allow_html=True)

company = st.text_input(
    "Company or Topic",
    placeholder="e.g. Tesla, Zomato, OpenAI, Indian EV Market...",
    label_visibility="collapsed"
)

c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    run_btn = st.button("🚀 Run Intelligence Report", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── Run Graph ───────────────────────────────────────────────────────────────
if run_btn and company.strip():

    with st.status("🤖 Multi-Agent Workflow Running...", expanded=True) as status:
        st.write("📋 **Manager** — Planning the BI research strategy...")
        st.write("🔬 **Research Supervisor** — Assigning search tasks to workers...")
        st.write("🌐 **Web Search Worker** — Searching the internet...")
        st.write("📰 **News Worker** — Fetching latest news...")
        st.write("📈 **Analysis Supervisor** — Assigning analysis tasks...")
        st.write("💰 **Financial Worker** — Analyzing financial data...")
        st.write("🏢 **Competitor Worker** — Mapping competitors...")
        st.write("✍️ **Writer Supervisor** — Briefing writing workers...")
        st.write("📄 **Report Writer** — Writing full BI report...")
        st.write("⚡ **Executive Summary** — Condensing for leadership...")

        graph  = build_graph()
        result = graph.invoke({"company": company.strip()})
        status.update(label="✅ Intelligence Report Complete!", state="complete", expanded=False)

    st.markdown("---")

    # ── Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-card"><div class="metric-val">10</div><div class="metric-lbl">Agents Run</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><div class="metric-val">3</div><div class="metric-lbl">Layers</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><div class="metric-val">4</div><div class="metric-lbl">Web Searches</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><div class="metric-val">6</div><div class="metric-lbl">Analysis Sections</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Executive Summary (top — most important)
    st.markdown("### ⚡ Executive Summary")
    st.markdown('<div class="exec-box">', unsafe_allow_html=True)
    st.markdown(result.get("executive_summary", ""))
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Manager's Research Plan
    with st.expander("📋 Manager's Research Plan (Layer 1 output)"):
        st.markdown(result.get("research_plan", ""))

    # ── Research Worker Outputs
    with st.expander("🌐 Web Research + 📰 News (Layer 3 — Research Workers)"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🌐 Web Research**")
            st.markdown(result.get("web_research", ""))
        with col2:
            st.markdown("**📰 Latest News**")
            st.markdown(result.get("news_research", ""))

    # ── Analysis Worker Outputs
    with st.expander("💰 Financial + 🏢 Competitor Analysis (Layer 3 — Analysis Workers)"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**💰 Financial Analysis**")
            st.markdown(result.get("financial_analysis", ""))
        with col2:
            st.markdown("**🏢 Competitor Analysis**")
            st.markdown(result.get("competitor_analysis", ""))

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Full Report
    st.markdown("### 📄 Full Business Intelligence Report")
    st.markdown('<div class="report-box">', unsafe_allow_html=True)
    st.markdown(result.get("full_report", ""))
    st.markdown("</div>", unsafe_allow_html=True)

    # ── Download
    st.markdown("<br>", unsafe_allow_html=True)
    full_output = (
        f"# Business Intelligence Report: {company}\n\n"
        f"## Executive Summary\n{result.get('executive_summary', '')}\n\n"
        f"## Full Report\n{result.get('full_report', '')}\n\n"
        f"## Financial Analysis\n{result.get('financial_analysis', '')}\n\n"
        f"## Competitor Analysis\n{result.get('competitor_analysis', '')}"
    )
    st.download_button(
        "⬇️ Download Full BI Report",
        data=full_output,
        file_name=f"BI_Report_{company.replace(' ', '_')}.md",
        mime="text/markdown"
    )

elif run_btn and not company.strip():
    st.warning("⚠️ Please enter a company name or topic.")

else:
    st.markdown("""
    <div style='text-align:center; padding:60px 20px; color:#333;'>
        <div style='font-size:3.5rem;'>📊</div>
        <div style='font-family: IBM Plex Mono, monospace; font-size:0.9rem; margin-top:14px; color:#555;'>
            Enter a company above and run the intelligence report
        </div>
        <div style='font-size:0.8rem; margin-top:8px; color:#333;'>
            10 agents across 3 layers will research, analyze, and report in minutes
        </div>
    </div>
    """, unsafe_allow_html=True)
