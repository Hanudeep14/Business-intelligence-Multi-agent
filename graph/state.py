from typing import TypedDict, List


class BIState(TypedDict):
    company: str                  
    research_plan: str            
    research_tasks: List[str]     
    web_research: str             
    news_research: str            
    analysis_tasks: List[str]     
    financial_analysis: str       
    competitor_analysis: str      
    writing_tasks: List[str]      
    full_report: str              
    executive_summary: str        
