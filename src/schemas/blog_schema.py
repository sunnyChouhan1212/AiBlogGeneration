from pydantic import BaseModel, Field


class BlogRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Topic for blog generation",
        example="Agentic AI",
    )