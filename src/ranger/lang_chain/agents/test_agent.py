import os
import getpass
import uuid 

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

from ranger.lib.anthropic_details import AnthropicDetails
from ranger.lang_chain.tools.info import info
from ranger.lang_chain.tools.math import math

anthropic = AnthropicDetails()
claude_sonnet_latest_model = anthropic.claude_sonnet_latest_model()

class TestAgent:
  """
  Test Ranger LangChain Agent
  """
  def __init__(self, ):
      self.tools = [info, math]
      self.memory = MemorySaver()
      self.query = "answer 12 times 12"
      self.content = {
    "role": "user",
    "content": self.query
    }
      pass

  def run(self, ):
    ai_agent = create_agent(
        model=claude_sonnet_latest_model,
        prompt=self.query,
        tools=self.tools,
        checkpointer=self.memory
        )
    config = {
        "configurable": {
            "thread_id": str(uuid.uuid1())
            }
            }
    for step in ai_agent.stream(
    {"messages": [("user", "yes")]},
    config, stream_mode="values"
    ):
      step["messages"][-1].pretty_print()

if __name__ == '__main__':
   TestAgent().run()