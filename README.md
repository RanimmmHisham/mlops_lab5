# 🚀 Local AI Thinking Assistant (MLOps Lab 5)

This project provides a web-based Graphical User Interface (GUI) to interact with local Large Language Models (LLMs) using **Ollama** and **Gradio**. It is specifically optimized for reasoning models like `qwen3:0.6b` to assist with technical MLOps tasks.

## 🛠️ Features
* **Local Inference:** All data stays on your machine via Ollama.
* **Web Interface:** Easy-to-use Gradio UI for chatting and experimentation.
* **MLOps Ready:** Structured to be easily containerized or integrated into automated workflows.

## 📋 Prerequisites
Before running the application, ensure you have the following installed:
1. **Python 3.9+**
2. **Ollama** ([Download here](https://ollama.com/))
3. **Git**

## 🚀 Getting Started

### 1. Set up the Model
Open your terminal and pull the required model:
```bash
ollama pull qwen3:0.6b
