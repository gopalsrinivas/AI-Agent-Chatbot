# FastAPI framework for creating the web application
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from langchain_community.tools.tavily_search import TavilySearchResults
import os
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

MODEL_NAMES = ["llama3-70b-8192", "mixtral-8x7b-32768"]

# Initialize the TavilySearchResults tool
tool_tavily = TavilySearchResults(max_results=2)
tools = [tool_tavily]

app = FastAPI(title="LangGraph AI Agent")


class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]


@app.post("/chat")
def chat_endpoint(request: RequestState):
    try:
        if request.model_name not in MODEL_NAMES:
            raise HTTPException(
                status_code=400,
                detail="Invalid model name. Please select a valid model.",
            )

        # Initialize the LLM
        llm = ChatGroq(groq_api_key=groq_api_key, model_name=request.model_name)

        # Create the ReAct agent
        agent = create_react_agent(
            llm, tools=tools, state_modifier=request.system_prompt
        )

        # Create the state
        state = {"messages": request.messages}

        # Process the state
        result = agent.invoke(state)

        return result
    except HTTPException as e:
        raise e  # Forward HTTP exceptions to the client
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
