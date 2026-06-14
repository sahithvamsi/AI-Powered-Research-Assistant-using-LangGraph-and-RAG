from typing import TypedDict, List


class ResearchState(TypedDict):
    query: str
    sub_questions: List[str]
    sources: List[dict]
    report: str
    review: str
    quality_score: int
    revision_count: int
    references: list