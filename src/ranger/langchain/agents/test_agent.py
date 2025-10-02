import os
import getpass
import uuid 

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

from lib.anthropic_details import AnthropicDetails
from tools.info import info
from tools.math import math

anthropic = AnthropicDetails()
claude_sonnet_latest_model = anthropic.claude_sonnet_latest_model()

if not os.getenv("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("enter anthropic api key")

tools = [info, math]
memory = MemorySaver()

query = "answer 12 times 12"

content = {
    "role": "user",
    "content": query
}
print("=" * 50)

ai_agent = create_agent(
    model=claude_sonnet_latest_model,
    prompt=query,
    tools=tools,
    checkpointer=memory

)
config = {
    "configurable": {
        "thread_id": f"{uuid.uuid1}"
    }
}
print(ai_agent.invoke({"messages": [content]})["messages"][-1].content)

for step in ai_agent.stream(
    {"messages": [("user", "info")]},
    config, stream_mode="values"
):
    print(step["messages"][-1].pretty_print())