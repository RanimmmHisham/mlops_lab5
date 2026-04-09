import gradio as gr
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:0.6b"

def chat_with_model(prompt):
    full_prompt = f"""
    <system>
    You are an expert AI assistant with advanced reasoning capabilities. 
    When a user asks a question, follow these steps:
    1. Analyze the core requirements of the request.
    2. Think step-by-step to arrive at the most logical conclusion.
    3. Provide a clear explanation followed by concrete, practical examples.
    4. If the request involves code or technical steps, ensure they follow MLOps best practices.
    </system>
    <user_query>
    {prompt}
    </user_query>
    <thought_process>
    </thought_process>
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": full_prompt,
            "stream": False
        }
    )

    result = response.json()
    return result.get("response", "No response from model")


iface = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(
        lines=5,
        placeholder="Ask me something like: Explain Docker in simple terms..."
    ),
    outputs=gr.Textbox(label="Response"),
    title="Local AI Thinking Assistant",
    description="Ask me anything and get clear explanations!"
)

if __name__ == "__main__":
    iface.launch()