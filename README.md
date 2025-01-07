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

# Docker build:

docker build -t langgraph-agent-app .

# Docker run:

docker run -p 8000:8000 -p 8501:8501 --name langgraph-agent-container langgraph-agent-app

# Docker build and run command

docker build -t langgraph-agent-app . && docker run -p 8000:8000 -p 8501:8501 --name langgraph-agent-container langgraph-agent-app

## Remove the existing container

# Stop the existing container

docker stop langgraph-agent-container

# Remove the existing container

docker rm langgraph-agent-container

# Run the container again

docker run -p 8000:8000 -p 8501:8501 --name langgraph-agent-container langgraph-agent-app

# Log in to Docker Hub

docker login

# Add tag image

docker tag langgraph-agent-app gopalsrinivas/langgraph-agent-app:latest

# Push the tagged image to Docker Hub

docker push gopalsrinivas/langgraph-agent-app:latest

## Pull the tagged image to Docker Hub

docker pull gopalsrinivas/langgraph-agent-app:latest
