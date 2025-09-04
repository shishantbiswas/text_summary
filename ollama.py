from ollama import chat
from ollama import ChatResponse
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 100
    min_length: int = 30

@app.get("/")
def root():
    return "ok"


@app.post("/")
def summarize(request: SummarizeRequest):
    input_text = "summarize: " + request.text
    response: ChatResponse = chat(model='gemma3:270m', messages=[
      {
        'role': 'user',
        'content': input_text,
      },
    ])
    return response.message.content