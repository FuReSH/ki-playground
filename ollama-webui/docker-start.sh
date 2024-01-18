#!/bin/bash

docker run -d \
    --network=host \
    -v ollama-webui:/app/backend/data \
    -e OLLAMA_API_BASE_URL=http://127.0.0.1:11434/api \
    --name ollama-webui \
    --restart always \
    ghcr.io/ollama-webui/ollama-webui:main