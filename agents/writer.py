import re

from llm.groq_client import ask_llm


def generate_report(
    query: str,
    sources: list,
    review=None
):
    source_text = ""
    references = []
    source_id = 1
    seen_urls = set()

    # ==========================================
    # BUILD SOURCE CONTEXT
    # ==========================================

    for item in sources:

        source_text += f"\nQUESTION: {item['question']}\n"

        for source in item["sources"][:3]:

            title = source.get(
                "title",
                "Unknown Source"
            )

            url = source.get(
                "href",
                source.get("url", "")
            )

            url = (
                url.strip()
                .strip('"')
                .strip("'")
            )

            content = source.get(
                "body",
                ""
            )[:250]

            source_text += f"""

SOURCE_ID: {source_id}

TITLE:
{title}

URL:
{url}

CONTENT:
{content}

"""

            if url and url not in seen_urls:

                references.append(
                    {
                        "id": source_id,
                        "title": title,
                        "url": url
                    }
                )

                seen_urls.add(url)

            source_id += 1

    # ==========================================
    # REVIEW FEEDBACK
    # ==========================================

    feedback = ""

    if review:

        feedback = f"""

CRITIC FEEDBACK

{review}

Improve the report using this feedback.
"""

    # ==========================================
    # PROMPT
    # ==========================================

    prompt = f"""
You are a Senior Research Analyst.

Research Question:

{query}

EVIDENCE SOURCES

{source_text}

{feedback}

Write a professional research report.

FORMAT

# Executive Summary

# Background

# Analysis

# Risks

# Opportunities

# Key Findings

# Conclusion

RULES

1. Use only provided evidence.
2. DO NOT create a References section. and Use citations like [1], [2], [3].
3. Every factual claim should have a citation.
4. Never invent facts.
5. Use markdown headings.
6. Keep the report professional.
7. Return only the report.
"""

    # ==========================================
    # GENERATE REPORT
    # ==========================================

    report = ask_llm(
        prompt=prompt,
        temperature=0.2,
        max_tokens=1500
    )

    # ==========================================
    # MAKE CITATIONS CLICKABLE
    # ==========================================

    main_report = report

    for ref in references:

        safe_url = (
            ref["url"]
            .replace('"', '')
            .replace("'", "")
            .strip()
        )

        main_report = re.sub(
            rf"\[{ref['id']}\]",
            f'<a href="{safe_url}" target="_blank">[{ref["id"]}]</a>',
            main_report
        )

    report = main_report

    # ==========================================
    # REFERENCES SECTION
    # ==========================================

    #report += "\n\n# References\n"

    for ref in references:

        report += f"""

[{ref['id']}] {ref['title']}

{ref['url']}
"""

    # DEBUG
    print(report[:3000])

    return {
        "report": report,
        "references": references
    }