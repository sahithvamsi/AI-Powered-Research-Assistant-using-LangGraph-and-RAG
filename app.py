import os
import re
import streamlit as st

from graph.workflow import app

from memory.memory_manager import (
    load_memory,
    save_report
)

from exports.pdf_exporter import export_pdf
from exports.docx_exporter import export_docx

from rag.chat import answer_report_question


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Research Platform",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 AI Research Platform")

st.caption(
    "Generate professional AI-powered research reports"
)


# =====================================================
# LOAD MEMORY
# =====================================================

reports = load_memory()


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("📚 Research History")

    search = st.text_input(
        "Search Reports"
    )

    filtered_reports = reports

    if search:

        filtered_reports = [
            item
            for item in reports
            if search.lower()
            in item["query"].lower()
        ]

    st.divider()

    for item in reversed(filtered_reports):

        if st.button(
            item["query"][:50],
            key=f"history_{item['query']}"
        ):

            st.session_state["report"] = (
                item["report"]
            )

    st.divider()

    if st.button(
        "🗑 Clear History",
        use_container_width=True
    ):

        with open(
            "memory/reports.json",
            "w",
            encoding="utf-8"
        ) as f:

            f.write("[]")

        st.rerun()


# =====================================================
# QUERY INPUT
# =====================================================

query = st.text_area(
    "Research Topic",
    height=120,
    placeholder="""
Examples:

AI Startups in Healthcare

Electric Vehicle Market

Hair Oil Industry in India
"""
)

generate = st.button(
    "🚀 Generate Report",
    use_container_width=True
)


# =====================================================
# GENERATE REPORT
# =====================================================

if generate:

    if not query.strip():

        st.warning(
            "Please enter a research topic."
        )

    else:

        with st.spinner(
            "Researching..."
        ):

            result = app.invoke(
                {
                    "query": query,
                    "sub_questions": [],
                    "sources": [],
                    "report": "",
                    "review": "",
                    "quality_score": 0,
                    "revision_count": 0
                }
            )

            report = result["report"]

            pdf_report = re.sub(
               r'<[^>]+>',
                 '',
               report
           )

            pdf_path = export_pdf(
            pdf_report,
                  query
                       )

            docx_path = export_docx(
    report,
    query
)

            save_report(
                query=query,
                report=report,
                pdf_path=pdf_path,
                source_count=len(
                    result.get(
                        "sources",
                        []
                    )
                )
            )

            st.session_state["report"] = report
            st.session_state["pdf"] = pdf_path
            st.session_state["docx"] = docx_path

        st.success(
            "✅ Research Completed"
        )



# =====================================================
# DISPLAY REPORT
# =====================================================

if "report" in st.session_state:

    report = st.session_state["report"]

    refs = re.findall(
        r"https?://[^\s]+",
        report
    )

    unique_refs = list(
        dict.fromkeys(refs)
    )

    citations = len(
        re.findall(
            r"\[\d+\]",
            report
        ) 
    )

    words = len(
        report.split()
    )

    # =================================================
    # ANALYTICS
    # =================================================

    st.subheader("📊 Analytics")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Words",
        f"{words:,}"
    )

    c2.metric(
        "Sources",
        len(unique_refs)
    )

    c3.metric(
        "Citations",
        citations
    )

    st.divider()

    # =================================================
    # TABS
    # =================================================

    tab1, tab2 = st.tabs(
    [
        "📄 Report",
        "💬 Chat"
    ]
)
    # =================================================
    # REPORT TAB
    # =================================================

    with tab1:

        st.markdown(report,unsafe_allow_html=True
)

        st.divider()

        st.subheader(
            "📥 Downloads"
        )

        d1, d2 = st.columns(2)

        if "pdf" in st.session_state:

            with d1:

                with open(
                    st.session_state["pdf"],
                    "rb"
                ) as f:

                    st.download_button(
                        "📄 Download PDF",
                        data=f,
                        file_name=os.path.basename(
                            st.session_state["pdf"]
                        ),
                        mime="application/pdf",
                        use_container_width=True
                    )

        if "docx" in st.session_state:

            with d2:

                with open(
                    st.session_state["docx"],
                    "rb"
                ) as f:

                    st.download_button(
                        "📘 Download DOCX",
                        data=f,
                        file_name=os.path.basename(
                            st.session_state["docx"]
                        ),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        use_container_width=True
                    )

    # =================================================

    # =================================================
    # CHAT TAB
    # =================================================

    with tab2:

        st.subheader(
            "💬 Chat With Report"
        )

        question = st.text_input(
            "Ask a question about this report"
        )

        if question:

            with st.spinner(
                "Thinking..."
            ):

                answer = answer_report_question(
                    report,
                    question
                )

            st.success(answer)