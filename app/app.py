import gradio as gr
import openai
import config

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages= history_openai_format,
        temperature=1.0,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if len(chunk['choices'][0]['delta']) != 0:
            partial_message = partial_message + chunk['choices'][0]['delta']['content']
            yield partial_message

gr.ChatInterface(
        predict,
        title="KDH KI Playground: ChatGPT",
        description="Führen Sie einen Dialog mit ChatGPT. Disclaimer: Die Daten werden im Hintergrund an OpenAI übertragen.",
        examples=["Schreibe mir eine Gliederung für eine wissenschaftliche Hausarbeit für das Seminar X.", "Schreibe mir eine Gliederung für einen wissenschaftlichen Artikel zu meinem Spezialgebiet.", "Bitte schickt Smilies :)"],
        clear_btn="Löschen",
        undo_btn="Rückgängig",
        retry_btn="Wiederholen"
    ).queue().launch(share=True)
