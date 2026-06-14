import json
import os
from datetime import datetime

MEMORY_FILE = "memory/reports.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return []


def save_report(
    query,
    report,
    pdf_path="",
    source_count=0
):

    memory = load_memory()

    for item in memory:

        if item["query"].lower() == query.lower():

            item["report"] = report
            item["pdf_path"] = pdf_path

            item["source_count"] = source_count

            item["word_count"] = len(
                report.split()
            )

            item["updated_at"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            with open(
                MEMORY_FILE,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    memory,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

            return

    memory.append({

        "query": query,

        "summary": report[:300],

        "report": report,

        "pdf_path": pdf_path,

        "source_count": source_count,

        "word_count": len(
            report.split()
        ),

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    })

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memory,
            f,
            indent=4,
            ensure_ascii=False
        )


def get_related_reports(
    query,
    limit=3
):

    memory = load_memory()

    matches = []

    query_words = query.lower().split()

    for item in memory:

        stored_query = item.get(
            "query",
            ""
        ).lower()

        if any(
            word in stored_query
            for word in query_words
        ):
            matches.append(item)

    return matches[-limit:]


def build_memory_context(
    query
):

    reports = get_related_reports(
        query
    )

    if not reports:
        return ""

    context = "\n\nPREVIOUS RESEARCH:\n"

    for i, item in enumerate(
        reports,
        start=1
    ):

        context += f"""

Report {i}

Query:
{item['query']}

{item['report'][:1000]}

"""

    return context