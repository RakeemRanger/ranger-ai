import os
import getpass
import uuid 

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

from ranger.lib.anthropic_details import AnthropicDetails
from ranger.lang_chain.tools.info import info
from ranger.lang_chain.tools.math import math

class TestAgent:
    """
    Test Ranger LangChain Agent with Chat Support
    """
    def __init__(self):
        self.tools = [info, math]
        self.memory = MemorySaver()
        self.anthropic = AnthropicDetails()
        self.model = self.anthropic.claude_sonnet_latest_model()
        self.agent = None
        self.config = {
            "configurable": {
                "thread_id": str(uuid.uuid4())
            }
        }
        self._initialize_agent()
    
    def _initialize_agent(self):
        """Initialize the LangGraph agent"""
        self.agent = create_agent(
            model=self.model,
            tools=self.tools,
            checkpointer=self.memory
        )
    
    def chat(self, message: str) -> str:
        """Chat interface for the agent"""
        try:
            result = self.agent.invoke(
                {"messages": [("user", message)]},
                config=self.config
            )
            return result["messages"][-1].content
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def stream_chat(self, message: str):
        """Streaming chat interface"""
        for step in self.agent.stream(
            {"messages": [("user", message)]},
            config=self.config,
            stream_mode="values"
        ):
            yield step["messages"][-1].content

if __name__ == '__main__':
    agent = TestAgent()
    print("Ranger AI Assistant initialized!")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        response = agent.chat(user_input)
        print(f"Assistant: {response}")