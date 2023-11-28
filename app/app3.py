
# testing huggingface inference api

import gradio as gr

from transformers import pipeline

pipe = pipeline("text-generation", model="gpt2")

def predict(text):
  return pipe(text)[0]["translation_text"]

demo = gr.ChatInterface(
  fn=predict,
  inputs='text',
  outputs='text',
)

demo.launch()


#demo = gr.load("gpt2-XL", src="models")

