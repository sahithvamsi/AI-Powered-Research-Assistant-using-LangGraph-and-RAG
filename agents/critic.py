from llm.groq_client import ask_llm


def review_report(report: str):

    prompt = f"""
You are a senior research reviewer.

Review the report.

Check:

1. Missing evidence
2. Missing citations
3. Weak logic
4. Unsupported claims
5. Missing risks
6. Missing opportunities
7. Missing future outlook

Return JSON:

{{
    "quality_score": 0,
    "missing_citations": [],
    "weak_sections": [],
    "improvements": []
}}

REPORT:

{report}
"""

    return ask_llm(
        prompt=prompt,
        temperature=0.1,
        max_tokens=1000
    )