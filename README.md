# 🔬 AI-Powered Research Assistant using LangGraph and RAG

An intelligent multi-agent research platform that automates report generation using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and LangGraph workflows.

The system performs web research, generates structured reports, stores research history, supports semantic retrieval using FAISS, enables report-based question answering, and exports reports as PDF and DOCX.

---

## 🚀 Features

- 🤖 Multi-Agent workflow using LangGraph
- 🔍 Retrieval-Augmented Generation (RAG)
- 🧠 Semantic Search using FAISS
- 📚 Research History & Memory
- 💬 Chat with Generated Reports
- 📄 PDF Export
- 📘 DOCX Export
- 📊 Report Analytics
- 🌐 Automated Web Research
- 📝 Citation Generation

---

## 🏗️ System Architecture

```text
                User Query
                     │
                     ▼
            Streamlit User Interface
                     │
                     ▼
              LangGraph Workflow
                     │
 ┌───────────────────┼───────────────────┐
 ▼                   ▼                   ▼
Planner Agent   Research Agent    Review Agent
                     │
                     ▼
              Report Generation
                     │
        ┌────────────┼────────────┐
        ▼                         ▼
  Memory Storage             PDF/DOCX Export
(JSON + FAISS)                     │
        │                          ▼
        ▼                   Download Reports
  RAG Chat Interface
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### AI & LLM
- LangGraph
- LangChain
- OpenAI/Groq LLMs

### Retrieval
- FAISS
- Embeddings

### Export
- ReportLab (PDF)
- python-docx (DOCX)

### Storage
- JSON Memory
- Pickle Serialization

---

## 📂 Project Structure

```text
ai-powered-research-assistant-using-langgraph-and-rag/
│
├── app.py
├── graph/
│   └── workflow.py
│
├── rag/
│   ├── chat.py
│   └── vector_store.py
│
├── memory/
│   ├── memory_manager.py
│   └── reports.json
│
├── exports/
│   ├── pdf_exporter.py
│   └── docx_exporter.py
│
├── data/
│   ├── report_index.faiss
│   └── report_chunks.pkl
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

### Step 1: User enters research topic

Example:

```text
How will AI transform global labor markets and employment patterns?
```

### Step 2: LangGraph executes workflow

```text
Query
   ↓
Planner
   ↓
Research Agent
   ↓
Writer
   ↓
Reviewer
   ↓
Final Report
```

### Step 3: Report generation

- Collects information
- Creates citations
- Formats report

### Step 4: Store memory

Reports are stored in:

```text
memory/reports.json
```

Embeddings are stored in:

```text
data/report_index.faiss
```

### Step 5: Export

Reports can be downloaded as:

- PDF
- DOCX

### Step 6: Chat with Report

Users can ask questions about generated reports using RAG.

---

## 🧠 Retrieval-Augmented Generation (RAG)

The system follows the RAG pipeline:

```text
User Question
      ↓
Retrieve Relevant Context
      ↓
FAISS Similarity Search
      ↓
LLM
      ↓
Generated Answer
```

This improves factual accuracy and reduces hallucinations.

---

## 📊 Analytics Dashboard

The platform automatically calculates:

- Total Words
- Number of Sources
- Number of Citations

Example:

```text
Words: 664
Sources: 17
Citations: 24
```

---

## 📄 PDF & DOCX Export

Generated reports can be exported as:

- PDF using ReportLab
- DOCX using python-docx

Hyperlinks and citations are preserved during export.

---

## 💬 Chat with Report

Ask contextual questions such as:

```text
What are the major findings of this report?

Which industries are most affected by AI?

Summarize the key recommendations.
```

The system retrieves relevant report sections and generates answers using RAG.

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ai-powered-research-assistant-using-langgraph-and-rag.git
```

### Navigate to Project

```bash
cd ai-powered-research-assistant-using-langgraph-and-rag
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔮 Future Enhancements

- Multi-user authentication
- Cloud database integration
- Advanced RAG pipelines
- Hybrid search (BM25 + Vector Search)
- Report comparison
- Real-time web search
- Agent specialization
- Dashboard visualizations

---

## 🎯 Use Cases

- Academic Research
- Market Analysis
- Industry Reports
- Company Analysis
- Technology Research
- Financial Research

---

## 👨‍💻 Author

**Sahith Vamsi Gandrala**

Built with ❤️ using LangGraph, RAG, FAISS, and Streamlit.
