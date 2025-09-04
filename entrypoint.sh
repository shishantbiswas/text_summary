#!/bin/bash
set -e

# Start ollama server in the background
ollama serve &

# Wait for the server to be ready
echo "Waiting for Ollama server to start..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 2
done

# Pull model if not already available
ollama pull gemma3:270m || true

# Start FastAPI app
exec uvicorn app:app --host 0.0.0.0 --port 8000
