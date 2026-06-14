from langgraph.graph import StateGraph, END

from graph.state import ResearchState

from graph.nodes import (
    planner_node,
    searcher_node,
    writer_node,
    critic_node
)


def should_continue(state):

    if state["quality_score"] >= 85:
        return "end"

    if state["revision_count"] >= 3:
        return "end"

    return "rewrite"


graph = StateGraph(
    ResearchState
)

graph.add_node(
    "planner",
    planner_node
)

graph.add_node(
    "searcher",
    searcher_node
)

graph.add_node(
    "writer",
    writer_node
)

graph.add_node(
    "critic",
    critic_node
)

graph.set_entry_point(
    "planner"
)

graph.add_edge(
    "planner",
    "searcher"
)

graph.add_edge(
    "searcher",
    "writer"
)

graph.add_edge(
    "writer",
    "critic"
)

graph.add_conditional_edges(
    "critic",
    should_continue,
    {
        "rewrite": "writer",
        "end": END
    }
)

app = graph.compile()