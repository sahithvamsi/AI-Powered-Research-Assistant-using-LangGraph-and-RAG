import json

from agents.planner import generate_subquestions
from agents.searcher import collect_sources
from agents.writer import generate_report
from agents.critic import review_report


def planner_node(state):

    sub_questions = generate_subquestions(
        state["query"]
    )

    return {
        **state,
        "sub_questions": sub_questions
    }


def searcher_node(state):

    sources = collect_sources(
        state["sub_questions"]
    )

    return {
        **state,
        "sources": sources
    }


def writer_node(state):

    writer_result = generate_report(
        query=state["query"],
        sources=state["sources"],
        review=state.get("review")
    )

    return {
        **state,
        "report": writer_result["report"],
        "references": writer_result["references"],
        "revision_count": state.get(
            "revision_count",
            0
        ) + 1
    }


def critic_node(state):

    review = review_report(
        state["report"]
    )

    score = 0

    try:
        data = json.loads(review)

        score = data.get(
            "quality_score",
            0
        )

    except Exception:
        pass

    return {
        **state,
        "review": review,
        "quality_score": score
    }