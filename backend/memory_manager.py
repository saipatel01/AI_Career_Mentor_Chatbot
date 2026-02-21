import streamlit as st

def initialize_memory():
    """
    Initialize chat history in session state
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_message(role, content):
    """
    Add message to chat history
    """
    st.session_state.messages.append((role, content))

def get_messages():
    """
    Retrieve chat history
    """
    return st.session_state.messages