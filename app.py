import streamlit as st
from backend.memory_manager import initialize_memory, add_message, get_messages
from backend.chat_controller import ChatController

# Page configuration
st.set_page_config(page_title="AI Career Mentor", layout="wide")

st.title("AI Career Mentor")
st.write("Ask your Generative AI career or internship related questions.")

# Initialize memory
initialize_memory()

# Initialize controller once
if "controller" not in st.session_state:
    st.session_state.controller = ChatController()

controller = st.session_state.controller

# Display chat history
for role, message in get_messages():
    with st.chat_message(role):
        st.markdown(message, unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your question here...")

if user_input:
    add_message("user", user_input)

    with st.spinner("Analyzing your career path..."):
        response = controller.get_response(user_input)

    add_message("assistant", response)

    st.rerun()