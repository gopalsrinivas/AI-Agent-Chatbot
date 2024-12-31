# AI-Agent-Chatbot

how to create a powerful AI chatbot using LangGraph, FastAPI, and Streamlit. We'll define a FastAPI backend endpoint to process requests, integrate LangGraph agents with dynamic model selection, and build an intuitive Streamlit UI for user interaction. Perfect for developers building interactive AI applications.

## Fastapi run command

uvicorn app:app --reload

## Request body:

{
"model_name": "mixtral-8x7b-32768",
"system_prompt": "you are a researcher",
"messages": [
"Give me the treands of AI in 2025"
]
}

Url : http://127.0.0.1:8000/docs

## UI command line

streamlit run ui.py

url :

http://localhost:8501/
