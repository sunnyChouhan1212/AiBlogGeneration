import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


class GroqLLM:
    """
    Groq LLM configuration and initialization.
    """

    def __init__(self) -> None:
        load_dotenv()

        self.groq_api_key = os.getenv("GROQ_API_KEY")

        if not self.groq_api_key:
            raise ValueError("GROQ_API_KEY is missing in .env file.")

    def get_llm(self) -> ChatGroq:
        """
        Initialize and return Groq LLM instance.
        """

        try:
            llm = ChatGroq(
                api_key=self.groq_api_key,
                model="llama-3.1-8b-instant",
                temperature=0,
            )

            return llm

        except Exception as error:
            raise RuntimeError(
                f"Error initializing Groq LLM: {error}"
            ) from error