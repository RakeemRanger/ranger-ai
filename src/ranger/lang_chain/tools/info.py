from ranger.lib.langchain_tools_client import tool


@tool
def info() -> str:
    """
    Provides information about the LLM application
    """
    return "I am Ranger LLM application"