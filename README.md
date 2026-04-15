# 📊 Business Intelligence Multi-Agent System

A **3-layer multi-agent orchestration system** built with **LangGraph** that performs deep business intelligence research on any company — using 10 specialized AI agents working in a Manager → Supervisor → Worker hierarchy.

---

## 🏗️ Architecture

```
USER INPUT (Company Name)
        ↓
┌─────────────────────┐
│   MANAGER AGENT     │  ← Layer 1: Plans the entire BI workflow
└────────┬────────────┘
         │
  ┌──────┴──────────────────┐
  ↓                         ↓                         ↓
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  RESEARCH    │   │  ANALYSIS    │   │   WRITER     │  ← Layer 2: Supervisors
│  SUPERVISOR  │   │  SUPERVISOR  │   │  SUPERVISOR  │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │                  │                  │
    ↓    ↓             ↓    ↓             ↓      ↓
 [Web] [News]    [Finance][Compete]   [Report][Summary]  ← Layer 3: Workers
```

---

## 🤖 All 10 Agents

| Layer | Agent | Role |
|---|---|---|
| 1 | **Manager** | Reads input, creates full research plan |
| 2 | **Research Supervisor** | Delegates web + news search tasks |
| 2 | **Analysis Supervisor** | Delegates financial + competitor tasks |
| 2 | **Writer Supervisor** | Delegates report + summary writing tasks |
| 3 | **Web Search Worker** | Live internet research via Tavily |
| 3 | **News Worker** | Fetches latest news |
| 3 | **Financial Worker** | Revenue, growth, financial metrics |
| 3 | **Competitor Worker** | Identifies and analyzes competitors |
| 3 | **Report Writer** | Full detailed BI report in Markdown |
| 3 | **Executive Summary** | CEO-ready concise summary |

---

## 🛠️ Tech Stack

- **LangGraph** — Multi-agent orchestration & state management
- **Groq (Llama 3.3 70B)** — Free, fast LLM
- **Tavily** — Real-time web search (4 searches total)
- **Streamlit** — Interactive web UI
- **Python** — Core language

---

## 🚀 Setup & Run

```bash
# 1. Clone
git clone https://github.com/yourusername/business-intelligence-agent.git
cd business-intelligence-agent

# 2. Virtual environment
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

# 3. Install
pip install -r requirements.txt

# 4. API Keys (.env file)
cp .env.example .env
# Add your free keys inside .env

# 5. Run
streamlit run app.py
```

---

## 🔑 Free API Keys

| Service | URL | Free Tier |
|---|---|---|
| Groq | https://console.groq.com | ✅ Free |
| Tavily | https://app.tavily.com | ✅ 1000/month free |

---

## 📁 Project Structure

```
business-intelligence-agent/
├── app.py                    ← Streamlit UI with live agent progress
├── graph/
│   ├── state.py              ← Shared BIState (TypedDict)
│   ├── nodes.py              ← All 10 agent node functions
│   └── workflow.py           ← LangGraph pipeline (3-layer)
├── tools/
│   └── search_tool.py        ← Tavily web search wrapper
├── .env.example
├── requirements.txt
└── README.md
```

---

## 💡 Key Concepts Demonstrated

- **3-layer multi-agent hierarchy** (Manager → Supervisor → Worker)
- **StateGraph orchestration** with 10 nodes and 9 edges
- **Supervisor pattern** — each supervisor plans & delegates to workers
- **Tool use** — Search workers call Tavily API (real internet)
- **State passing** — all agents share a typed state dict
- **Sequential pipeline** within each layer

---

## 📄 License

MIT License
