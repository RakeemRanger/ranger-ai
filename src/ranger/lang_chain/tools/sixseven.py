from ranger.lib.langchain_tools_client import tool
from ranger.lib.anthropic_details import AnthropicDetails
import os 

from anthropic import Anthropic

@tool
def anything(query: str) -> str:
    """
    Kyndall's Magical Answers
    """
    claude = AnthropicDetails()
    kyndall = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = kyndall.messages.create(
    model=claude.claude_sonnet_latest_model(),
    max_tokens=1000,
    messages=[
        {"role": "user", "content": query}
    ]
)
    return response