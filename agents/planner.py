import json
from llm.groq_client import ask_llm


def generate_subquestions(query: str):

    prompt = f"""
You are a research planner.

Break the following research question into 3 specific searchable sub-questions.

Return ONLY a JSON list of strings.

Question:
{query}
"""

    response = ask_llm(prompt)

    try:
        data = json.loads(response)

        if isinstance(data, list):
            return data

        return []

    except Exception:
        return [query]