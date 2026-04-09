import gradio as gr
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:0.6b"

def chat_with_model(prompt):
    full_prompt = f"You are a helpful AI assistant. Explain clearly with examples:\n{prompt}"

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": full_prompt,
            "stream": False
        }
    )

    result = response.json()
    return result["response"]

iface = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(
        lines=5,
        placeholder="Ask me something like: Explain Docker in simple terms..."
    ),
    outputs=gr.Textbox(label="Response"),
    title="💬 Local AI Thinking Assistant",
    description="Ask me anything and get clear explanations!"
)

if __name__ == "__main__":
    iface.launch()