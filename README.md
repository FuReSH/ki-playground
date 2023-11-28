## Playground for AI Chatbots

Mission: Provide basic access to three large language models (GPT-3.5, GPT-2, Llama2)

Solution: First iteration: Three separate Gradio apps, one for each model

## Docker Image

```bash
docker run --rm -it -p 7860:7860 -e GRADIO_SERVER_NAME=0.0.0.0
```
