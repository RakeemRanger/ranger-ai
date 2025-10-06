import base64
import random


import streamlit as st
from ranger.lang_chain.agents.test_agent import TestAgent


def get_base64_image(image_path):
    """Convert image to base64 string"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert your image to base64
icon_base64 = get_base64_image("/home/nodebrite/new/src/ranger/lib/fulllogo_transparent_nobuffer.png")

st.set_page_config(
    page_title="Kyndall AI Chatbot", 
    page_icon=f"data:image/png;base64,{icon_base64}",
    layout="wide"
)

# Fixed line 19 - Display the actual image in the title area
col1, col2 = st.columns([1, 8])
with col1:
    # Display the logo image
    st.image(f"data:image/png;base64,{icon_base64}", width=60)
with col2:
    st.title("Kyndall AI Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize agent
if "agent" not in st.session_state:
    st.session_state.agent = TestAgent()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

chat_intro = [
    "My name is Kyndall, your AI Assistant. What can I help you with today?",
    "I am Dartinbot's AI ChatBot Kyndall, task me with anything",
    "Its your girl Kyndall, What can I do for you?"
]
# React to user input
if prompt := st.chat_input(random.choice(chat_intro)):
    # Display user message in chat message container
    st.chat_message("user").markdown(f"""User Query: {prompt}""")

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.chat(prompt)
            st.code(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})