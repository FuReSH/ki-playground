from transformers import pipeline
import gradio as gr

pipe = pipeline("text-generation", model="NousResearch/Llama-2-7b-chat-hf")

demo = gr.Interface.from_pipeline(pipe)
demo.launch(share=True)

