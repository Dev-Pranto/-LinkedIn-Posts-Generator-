# 🚀 LinkedIn Post Generator AI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI Model](https://img.shields.io/badge/Model-Grok--3-purple)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)

A professional content generation tool powered by **xAI's Grok-3** (via GitHub Models). This application helps users generate structured, engaging, and multi-lingual LinkedIn posts in seconds.

## ✨ Features
* **Multi-Model Support:** Configured to run on Grok-3, GPT-4o, or any model compatible with Azure AI Inference.
* **Multi-Lingual:** Generates native-quality content in English, Bengali, Spanish, French, and more.
* **Secure:** Handles API credentials via `.env` or secure UI input.
* **One-Click Download:** Export generated posts as `.txt` files.

## 🛠️ Setup & Installation

1.  **Clone the Repo**
    ```bash
    git clone [https://github.com/Dev-Pranto/linkedin-ai-generator.git](https://github.com/Dev-Pranto/linkedin-ai-generator.git)
    cd linkedin-ai-generator
    ```

2.  **Install Requirements**
    ```bash
    pip install streamlit azure-ai-inference python-dotenv
    ```

3.  **Configure Environment**
    Create a `.env` file:
    ```env
    GITHUB_AI_ENDPOINT=[https://models.inference.ai.azure.com](https://models.inference.ai.azure.com)
    GITHUB_AI_TOKEN=your_github_token_here
    GITHUB_AI_MODEL=xai/grok-3
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 🧠 How it Works
This project uses the **Azure AI Inference SDK** to connect to GitHub's Model Marketplace. It utilizes a `ChatCompletionsClient` to send optimized system prompts to the LLM, ensuring the output follows strict business writing guidelines.

## 👨‍💻 Author
**SK Hamim Ishthiaque Pranto**
