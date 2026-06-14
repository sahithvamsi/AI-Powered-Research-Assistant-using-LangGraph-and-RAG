from tools.web_search import search_web


def score_source(source):

    score = 0

    url = (
        source.get("href")
        or source.get("url")
        or ""
    ).lower()

    content = source.get("body", "")

    trusted_domains = [
        ".gov",
        ".edu",
        "reuters",
        "bloomberg",
        "statista",
        "mckinsey",
        "gartner",
        "forbes",
    ]

    for domain in trusted_domains:

        if domain in url:
            score += 10

    score += min(len(content) // 200, 10)

    return score


def collect_sources(sub_questions):

    all_sources = []

    for question in sub_questions:

        results = search_web(
            query=question,
            max_results=8
        )

        results.sort(
            key=score_source,
            reverse=True
        )

        results = results[:3]

        all_sources.append(
            {
                "question": question,
                "sources": results
            }
        )

    return all_sources