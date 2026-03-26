from fastapi import FastAPI
from pydantic import BaseModel
from agent import generate_answer

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask_question(q: Query):
    answer = generate_answer(q.query)
    return {"response": answer}