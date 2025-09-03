from fastapi import FastAPI
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = FastAPI()

MODEL_PATH = "/home/shishant/code/sumray/text_summarization"

tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH, legacy=False)
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 100
    min_length: int = 30


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/summarize")
def summarize(request: SummarizeRequest):
    input_text = "summarize: " + request.text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(
        inputs,
        max_length=request.max_length,
        min_length=request.min_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return {"summary": summary}

