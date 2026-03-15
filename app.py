import os
import streamlit as st
from groq import Groq


if "GROQ_API_KEY" not in st.secrets:
    st.error("GROQ_API_KEY is missing in Streamlit Secrets.")
    st.stop()

api_key = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=api_key)
st.title("Beta Tumse Nahi Hoga AI")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """You are a brutally sarcastic Indian mom chatbot.
            You answer questions correctly but also roast the user.
            You constantly mock their laziness, bad habits, procrastination, and poor life choices.
            You often compare them to 'Sharma ji ka beta'.
            Your tone should be sarcastic, slightly demotivating, and very funny.
            Keep responses short and witty."""
        }
    ]
        

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
prompt = st.chat_input("Ask something...")

if prompt:

    st.chat_message("user").write(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
