FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl wget \
    git git-lfs \
    && git lfs install \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir transformers torch fastapi uvicorn protobuf sentencepiece

RUN git clone https://huggingface.co/Falconsai/text_summarization /app/model

COPY main.py /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
