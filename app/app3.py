from transformers import pipeline
import gradio as gr

pipe = pipeline("text-generation", model="gpt2")

demo = gr.Interface.from_pipeline(pipe)
demo.launch(share=True)

