# AI Market Insight Assistant (Agentic RAG System)

## Overview

The AI Market Insight Assistant is an intelligent system designed to provide market insights using a combination of Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

The system improves response accuracy by retrieving relevant information from a custom knowledge base (FAISS vector store) and combining it with LLM-generated answers.

---

## Key Features

* Context-aware responses using Retrieval-Augmented Generation (RAG)
* FastAPI-based backend for real-time API interaction
* Integration with OpenAI models using LangChain
* Semantic search powered by FAISS vector database
* Custom knowledge ingestion through text data
* REST API endpoint for querying insights

---

## System Architecture

User Query → FastAPI → Agent (LLM) → RAG (FAISS Search) → Context Injection → Final Response

---

## Tech Stack

* Programming Language: Python
* Framework: FastAPI
* LLM Integration: LangChain
* Model Provider: OpenAI
* Vector Database: FAISS
* Environment: Anaconda, Jupyter Notebook

---

## Project Structure

```
market-ai-assistant/
│
├── app.py
├── agent.py
├── rag.py
├── data.txt
├── requirements.txt
├── README.md
└── .env
```

---

## Installation and Setup

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Market-Insight-Assistant.git
cd AI-Market-Insight-Assistant
```

### Create Environment

```bash
conda create -p venv python=3.10 -y
conda activate venv
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add API Key

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

Open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

---

## API Usage

### Endpoint

POST /ask

### Sample Request

```json
{
  "query": "What are current AI market trends?"
}
```

### Sample Response

```json
{
  "response": "AI is rapidly growing in healthcare, finance, and generative AI sectors."
}
```

---

## Use Cases

* Market trend analysis
* Business intelligence support
* AI-powered knowledge assistant
* Decision-making insights

---

## Future Enhancements

* Add web interface using Streamlit
* Deploy on cloud platforms
* Integrate real-time datasets
* Extend to multi-agent architecture

---

## Author

Janhvi Kharat
AI/ML Enthusiast

---

## Conclusion

This project demonstrates how combining LLMs with RAG architecture can create accurate and context-aware AI systems for real-world applications.
