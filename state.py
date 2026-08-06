from typing import TypedDict

class AgentState(TypedDict):
    code:str
    review:str
    optimized_code:str
    explanation:str