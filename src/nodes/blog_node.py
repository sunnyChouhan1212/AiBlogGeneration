from src.states.blogstate import BlogState

class BlogNode:
    """
    Blog workflow nodes for LangGraph.
    """

    def __init__(self, llm) -> None:
        self.llm = llm

    
    def title_creation(self,state:BlogState)-> dict:
        """
        Generate SEO-friendly blog title.
        """

        topic = state.get("topic", "").strip()

        if not topic:
            raise ValueError("Topic is required for title generation.")

        prompt = f"""
            You are an expert blog content writer.

            Use Markdown formatting.

            Generate a creative and SEO-friendly blog title
            for the following topic:

            Topic: {topic}
        """
            
        sytem_message=prompt.format(topic=state["topic"])
        print(sytem_message)
        response=self.llm.invoke(sytem_message)
        print(response)
        return {
            "blog": {
                "title": response.content.strip(),
            }
        }
        
    def content_generation(self,state:BlogState)-> dict:
        """
        Generate detailed blog content.
        """

        topic = state.get("topic", "").strip()

        if not topic:
            raise ValueError("Topic is required for content generation.")

        blog = state.get("blog", {})
        title = blog.get("title", "").strip()

        if not title:
            raise ValueError("Blog title is required.")

        prompt = f"""
        You are an expert blog writer.

        Use Markdown formatting.

        Generate a detailed, well-structured blog post
        for the following topic.

        Include:
        - Introduction
        - Key Concepts
        - Examples
        - Benefits
        - Conclusion

        Topic: {topic}

        Blog Title: {title}
        """

        response = self.llm.invoke(prompt)

        return {
            "blog": {
                "title": title,
                "content": response.content.strip(),
            }
        }