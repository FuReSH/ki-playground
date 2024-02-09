from transformers import pipeline
import gradio as gr

pipe = pipeline("text-generation", model="gpt2", max_new_tokens=500)

demo = gr.Interface.from_pipeline(pipe)
demo.launch(share=True)

