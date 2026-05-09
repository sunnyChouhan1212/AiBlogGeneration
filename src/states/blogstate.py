from typing import TypedDict

from pydantic import BaseModel, Field


class Blog(BaseModel):
    """
    Blog response schema.
    """

    title: str = Field(
        ...,
        description="Title of the blog post",
        example="Introduction to Agentic AI",
    )

    content: str = Field(
        ...,
        description="Main content of the blog post",
        example="Agentic AI systems can reason and take actions...",
    )


class BlogState(TypedDict):
    """
    LangGraph state schema.
    """

    topic: str
    blog: Blog
    current_language: str