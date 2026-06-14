from ddgs import DDGS


def search_web(query, max_results=3):

    with DDGS() as ddgs:
        results = list(
            ddgs.text(
                query,
                max_results=max_results
            )
        )

    return results


def search_news(query, max_results=3):

    with DDGS() as ddgs:
        results = list(
            ddgs.news(
                query,
                max_results=max_results
            )
        )

    return results