# 🔬 AI-Powered Research Assistant using LangGraph and RAG

An intelligent multi-agent AI research platform that automates research report generation using Large Language Models (LLMs), LangGraph workflows, and Retrieval-Augmented Generation (RAG).

The platform performs autonomous research, generates structured reports with citations, stores research history, enables semantic retrieval using FAISS, supports report-based question answering, and exports reports as PDF and DOCX.

---

## 🚀 Live Demo

🌐 **Application:** https://ragproject345.streamlit.app/

---

## ✨ Features

- 🤖 Multi-Agent AI Workflow using LangGraph
- 🔍 Retrieval-Augmented Generation (RAG)
- 🧠 Semantic Search with FAISS
- 📚 Research History Management
- 💬 Chat with Generated Reports
- 📄 PDF Export
- 📘 DOCX Export
- 📊 Report Analytics Dashboard
- 🔗 Citation Generation
- 🌐 Automated Web Research
- 📝 Persistent Memory Storage

---

# 🏗️ System Architecture

```text
                           User
                             │
                             ▼
                  Streamlit User Interface
                             │
                             ▼
                        User Query
                             │
                             ▼
                    LangGraph Workflow
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
 Planner Agent       Research Agent      Review Agent
        │                    │                    │
        └────────────────────┼────────────────────┘
                             ▼
                       Writer Agent
                             │
                             ▼
                        Final Report
                             │
         ┌───────────────────┼───────────────────┐
         ▼                                       ▼
 Memory Management                         Export Module
(JSON + FAISS)                         (PDF / DOCX)
         │
         ▼
   RAG Retrieval
         │
         ▼
 Chat with Report
         │
         ▼
  Contextual Answers
```

---

# 🤖 Agents

## 1. Planner Agent

- Analyzes user query
- Generates sub-questions
- Plans research strategy

### Example

```text
Query:
"How will AI transform labor markets?"

Generated Sub-questions:

• Which jobs are at risk?
• What new jobs are emerging?
• Economic impact of AI?
```

---

## 2. Research Agent

- Collects information
- Retrieves sources
- Gathers evidence

---

## 3. Writer Agent

- Organizes findings
- Generates structured report
- Adds citations and references

---

## 4. Review Agent

- Evaluates report quality
- Checks completeness
- Improves coherence

---

# 🔄 Workflow

```text
User Query
    ↓
Planner Agent
    ↓
Research Agent
    ↓
Writer Agent
    ↓
Review Agent
    ↓
Final Report
    ↓
PDF / DOCX Export
    ↓
RAG Chat
```

---

# 🧠 RAG Pipeline

```text
User Question
      ↓
Chunking
      ↓
Embeddings
      ↓
FAISS Similarity Search
      ↓
Retrieve Relevant Chunks
      ↓
LLM
      ↓
Generated Answer
```

---

# 📂 Project Structure

```text
ai-powered-research-assistant-using-langgraph-and-rag/
│
├── app.py                          # Main Streamlit application
│
├── graph/
│   ├── workflow.py                # LangGraph workflow
│   └── state.py                   # Shared state definitions
│
├── agents/
│   ├── planner.py                 # Planner Agent
│   ├── researcher.py              # Research Agent
│   ├── writer.py                  # Writer Agent
│   └── reviewer.py                # Review Agent
│
├── rag/
│   ├── chat.py                    # Chat with report
│   ├── vector_store.py            # FAISS operations
│   └── embeddings.py              # Embedding generation
│
├── memory/
│   ├── memory_manager.py          # History management
│   └── reports.json               # Stored reports
│
├── exports/
│   ├── pdf_exporter.py            # PDF generation
│   └── docx_exporter.py           # DOCX generation
│
├── data/
│   ├── report_index.faiss         # FAISS index
│   └── report_chunks.pkl          # Stored chunks
│
├── requirements.txt
├── README.md
└── .env
```

---

# 🛠️ Tech Stack

### Frontend

- Streamlit

### AI Frameworks

- LangGraph
- LangChain

### LLM

- OpenAI / Groq

### Retrieval

- FAISS
- Embeddings

### Export

- ReportLab
- python-docx

### Storage

- JSON
- Pickle

---

# 📊 Analytics Dashboard

The application automatically calculates:

- Word Count
- Source Count
- Citation Count

Example:

```text
Words: 664
Sources: 17
Citations: 24
```

---

# 📄 Report Export

Reports can be exported as:

✅ PDF  
✅ DOCX  

Hyperlinks and citations are preserved.

---

# 💬 Chat with Report

Users can ask questions such as:

```text
What are the major findings?

Summarize the report.

What risks are discussed?

Which industries are most affected?
```

The system retrieves relevant context using FAISS and generates answers using RAG.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/ai-powered-research-assistant-using-langgraph-and-rag.git
```

## Navigate to Project

```bash
cd ai-powered-research-assistant-using-langgraph-and-rag
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Add Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
```

## Run Application

```bash
streamlit run app.py
```

---

# 🔮 Future Enhancements

- User Authentication
- Database Integration
- Hybrid Search (BM25 + Vector Search)
- Agent Collaboration
- Real-time Web Search
- Report Comparison
- Dashboard Visualizations
- Multi-user Support

---

# 🎯 Use Cases

- Academic Research
- Market Analysis
- Company Research
- Technology Trends
- Industry Reports
- Financial Analysis

---

# 👨‍💻 Author

**Sahith Vamsi Gandrala**

Built with ❤️ using LangGraph, RAG, FAISS, and Streamlit.
