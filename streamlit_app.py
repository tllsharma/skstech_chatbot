import streamlit as st
import openai
import os

# Set your OpenAI API key (or use environment variable)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# App title
st.set_page_config(page_title="💬 ChatBot AI")
st.title("🤖 AI ChatBot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Type your message...")

# Generate response
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                    messages=st.session_state.messages,
                )
                reply = response.choices[0].message["content"]
            except Exception as e:
                reply = "⚠️ Error: " + str(e)

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
