from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Sample market data (your knowledge base)
texts = [
    "Tesla stock is growing due to EV demand",
    "Reliance Industries is strong in energy sector",
    "Stock market is volatile in short term",
    "AI companies are seeing rapid growth",
    "Long-term investments are safer than short-term trading"
]

def create_vector_store():
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(texts, embeddings)

vectorstore = create_vector_store()

def search_data(query):
    return vectorstore.similarity_search(query)
    