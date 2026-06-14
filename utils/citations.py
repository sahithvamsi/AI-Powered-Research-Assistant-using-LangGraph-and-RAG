import re


def extract_citations(report):

    return re.findall(
        r"\[(\d+)\]",
        report
    )


def build_reference_map(references):

    citation_map = {}

    for ref in references:

        citation_map[
            str(ref["id"])
        ] = ref

    return citation_map