from langchain_openai import ChatOpenAI
from rag import load_knowledge

# Load LLM
llm = ChatOpenAI(temperature=0)

# Load RAG database
db = load_knowledge()

def generate_answer(query):
    # Search relevant docs
    docs = db.similarity_search(query)

    context = ""
    for doc in docs:
        context += doc.page_content + "\n"

    # Final prompt
    final_prompt = f"""
    You are an AI Market Insight Assistant.

    Use the below context to answer:

    Context:
    {context}

    Question:
    {query}

    Answer clearly:
    """

    response = llm.invoke(final_prompt)

    return response.content