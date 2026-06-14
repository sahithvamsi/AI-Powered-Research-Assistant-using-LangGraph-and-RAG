import os
import re

from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def export_pdf(
    report: str,
    query: str
):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    safe_query = re.sub(
        r"[^a-zA-Z0-9_]",
        "",
        query.replace(" ", "_")
    )

    filename = (
        f"{safe_query}_{timestamp}.pdf"
    )

    filepath = os.path.join(
        "reports",
        filename
    )

    pdf = SimpleDocTemplate(
        filepath
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Research Report",
            styles["Title"]
        )
    ) 

    elements.append(
        Spacer(1, 20) 
    )

    url_pattern = r"https?://[^\s]+"
    report = re.sub(
    r'<a href="([^"]+)" target="_blank">\[(\d+)\]</a>',
    r'<link href="\1">[\2]</link>',
    report
)

    for line in report.split("\n"):

        line = line.strip()

        if not line: 
            continue

        if line.startswith("#"):

            heading = (
                line.replace("#", "")
                .strip()
            )

            elements.append(
                Paragraph(
                    heading,
                    styles["Heading1"]
                )
            )  

        else:

            urls = re.findall(

                url_pattern,
                line
            )

            if urls:

                for url in urls:

                    elements.append(
                        Paragraph(
                            f'<link href="{url}">{url}</link>',
                            styles["BodyText"]
                        )
                    )

            else:

                elements.append(
                    Paragraph(
                        line,
                        styles["BodyText"]
                    )
                )

        elements.append(
            Spacer(1, 5)
        )

    pdf.build(elements)

    return filepath