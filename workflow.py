from langgraph.graph import StateGraph, START, END
from state import AgentState
from agents.reviewer import review_code
from agents.optimizer import optimize_code
from agents.explainer import explain_changes

def reviewer_node(state:AgentState):
    review = review_code(state["code"])
    
    return{
        "review":review
    }
    
def optimizer_node(state:AgentState):
    
    optimized_code=optimize_code(
        state["code"],
        state["review"]
        
    )
    return{
        "optimized_code":optimized_code
    }
    
def explainer_node(state:AgentState):
    explanation = explain_changes(
        state["code"],
        state["review"],
        state["optimized_code"]
    )
    
    return {
        "explanation":explanation
    }
graph = StateGraph(AgentState)

    
graph.add_node(
    "reviewer",
    reviewer_node
)
graph.add_node(
    "optimizer",
    optimizer_node
    
)
graph.add_node(
    "explainer",
    explainer_node
)
graph.add_edge(
    START,
    "reviewer"
)
graph.add_edge(
    "reviewer",
    "optimizer"
)
graph.add_edge(
    "optimizer",
    "explainer"
)
graph.add_edge(
    "explainer",
    END
)
workflow=graph.compile()