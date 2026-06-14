from llm.groq_client import ask_llm


def answer_report_question(
    report: str,
    question: str
):
    """
    Chat with a generated report.
    """

    prompt = f"""
You are an expert research assistant.

Use ONLY the report below.

REPORT:
{report}

QUESTION:
{question}

Rules:
- Answer only from the report.
- Do not invent information.
- If the answer is missing, say:
  "This information is not available in the report."
- Keep answers concise.
"""

    try:
        return ask_llm(prompt)

    except Exception as e:
        return f"Error: {str(e)}"