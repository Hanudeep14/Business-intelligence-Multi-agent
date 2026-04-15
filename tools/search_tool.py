import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()


def search_web(query: str, max_results: int = 3) -> str:
    """Search the web using Tavily and return formatted results as a string."""
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    response = client.search(
        query=query,
        max_results=max_results,
        include_answer=True,
        search_depth="basic"
    )

    output = ""
    for r in response.get("results", []):
        output += f"\n[{r.get('title', '')}] ({r.get('url', '')})\n"
        output += f"{r.get('content', '')[:400]}\n"

    return output.strip() or "No results found."
