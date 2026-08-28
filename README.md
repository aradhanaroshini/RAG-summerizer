# ✦ MainPoints

### Turn long documents into the points that actually matter.

**MainPoints** is a lightweight **Retrieval-Augmented Generation (RAG)** based document summarizer that extracts the most relevant information from lengthy documents and turns it into a concise, readable summary.

Instead of throwing an entire document at an LLM, MainPoints first **processes, chunks, embeds, and retrieves relevant content** before generating the final summary.

> **Less scrolling. More understanding.**

---

## ✨ What it does

MainPoints takes a document or webpage and follows a simple pipeline:

```text
📄 Document / 🌐 Webpage
          ↓
     Text Extraction
          ↓
    Smart Chunking
          ↓
   Semantic Embeddings
          ↓
      ChromaDB
          ↓
  Relevant Context Retrieval
          ↓
     LLM Summarization
          ↓
     ✦ Main Points
```

The result is a compact summary focused on the **key topics and information** within the source.

---

## 🚀 Features

* 📄 **Multiple input formats**

  * PDF
  * DOCX
  * TXT
  * Markdown
  * Web URLs

* 🧩 **Recursive text chunking** for handling long documents

* 🔎 **Semantic retrieval** instead of relying only on keyword matching

* 🧠 **Sentence-transformer embeddings** using `all-MiniLM-L6-v2`

* 🗃️ **Persistent vector storage** with ChromaDB

* 🤖 **LLM-powered summarization** using Groq + Llama 3.3 70B

* ⚡ **Lightweight CLI workflow** for quick experimentation

---

## 🛠️ Tech Stack

| Component              | Technology                           |
| ---------------------- | ------------------------------------ |
| Language               | Python                               |
| RAG                    | LangChain                            |
| Embeddings             | Hugging Face / Sentence Transformers |
| Vector Database        | ChromaDB                             |
| LLM                    | Groq — Llama 3.3 70B                 |
| PDF Processing         | PyPDF                                |
| DOCX Processing        | python-docx                          |
| Web Extraction         | BeautifulSoup                        |
| Environment Management | python-dotenv                        |

---

## 🧠 How the RAG pipeline works

### 1. Load

MainPoints accepts a file path or URL and extracts its textual content.

Supported inputs include:

```text
.pdf
.docx
.txt
.md
URL
```

### 2. Chunk

Long documents are divided into smaller overlapping sections using a recursive text splitter.

This helps preserve context while making the document easier to search.

### 3. Embed

Each chunk is converted into a numerical representation using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

### 4. Retrieve

The embeddings are stored in **ChromaDB**.

MainPoints then retrieves the chunks most relevant to the requested topic.

### 5. Summarize

The retrieved context is passed to an LLM through Groq, which generates a concise summary covering the important points.

---

## 💻 Getting Started

### Prerequisites

* Python 3.13+
* A Groq API key

### Clone the repository

```bash
git clone https://github.com/aradhanaroshini/MainPoints.git
cd MainPoints
```

### Install dependencies

```bash
pip install -r requirements.txt
```

> If you're using `uv`, install the dependencies defined for the project environment instead.

### Configure your API key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

**Never commit your `.env` file or API keys to GitHub.**

### Run

```bash
python main.py
```

You'll be prompted to provide the path to your document or webpage:

```text
Attach your path here:
```

Example:

```text
Attach your path here: ./documents/research_paper.pdf
```

or:

```text
Attach your path here: https://example.com/article
```

---

## 📁 Project Structure

```text
MainPoints/
│
├── main.py          # CLI entry point
├── dataset.py       # Document & webpage extraction
├── chunker.py       # Chunking, embeddings & retrieval
├── llm.py           # LLM-based summarization
├── pyproject.toml   # Project configuration
├── .gitignore
└── chroma_db/       # Persistent vector database
```

---

## 🎯 Why RAG?

Traditional summarization approaches can struggle when documents become large.

MainPoints uses a retrieval-first approach:

> **Retrieve what matters → Give the model the relevant context → Generate the summary**

This reduces unnecessary context and makes the summarization pipeline more targeted.

---

## 🔮 Roadmap

MainPoints is currently a CLI prototype, with several directions for future development:

* [ ] 🌐 Web interface
* [ ] 📚 Multiple-document summarization
* [ ] 💬 Ask questions about a document
* [ ] 📝 Custom summary lengths
* [ ] 🎯 User-defined topics
* [ ] 📑 Section-wise summaries
* [ ] 📊 Retrieval evaluation metrics
* [ ] 🔗 Source/citation tracking
* [ ] ⚡ Streaming responses

---

## 📌 Current Status

**Prototype / active development**

The current version focuses on establishing the core **document ingestion → retrieval → LLM summarization** pipeline.

---

## 👩‍💻 Author

**Aradhana Roshini**

Computer Science & Data Science
Interested in **AI • Data Science • Computational Biology • Research**

---

### ⭐ If MainPoints helped you understand a long document a little faster, consider giving the repository a star.

