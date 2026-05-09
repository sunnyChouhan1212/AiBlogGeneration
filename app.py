import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM
from src.schemas.blog_schema import BlogRequest

# Load environment variables
load_dotenv()

# Set LangSmith API Key
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

if langchain_api_key:
    os.environ["LANGSMITH_API_KEY"] = langchain_api_key


# Initialize FastAPI app
app = FastAPI(
    title="AI Blog Generator API",
    version="1.0.0",
    description="Generate blogs using LangGraph and Groq LLM",
)




# Initialize LLM once (better performance)
groq_llm = GroqLLM()
llm = groq_llm.get_llm()




@app.post("/blogs")
async def create_blogs(request: BlogRequest) -> dict:
    """
    Generate blogs based on topic.
    """

    topic = request.topic.strip()

    if not topic:
        raise HTTPException(
            status_code=400,
            detail="Topic cannot be empty.",
        )

    try:
        # Initialize Graph Builder once
        graph_builder = GraphBuilder(llm)
        graph = graph_builder.setup_graph(usecase="topic")

        state = graph.invoke(
            {
                "topic": topic,
            }
        )

        return {
            "success": True,
            "topic": topic,
            "data": state,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error


@app.get("/")
async def health_check() -> dict:
    """
    Health check endpoint.
    """

    return {
        "status": "running",
        "service": "AI Blog Generator API",
    }


def main() -> None:
    """
    Application entry point.
    """

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()