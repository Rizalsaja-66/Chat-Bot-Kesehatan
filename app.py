import streamlit as st
from chatbot_logic import HealthChatbot
import time

st.set_page_config(page_title="Chatbot Kesehatan", page_icon="🩺")

# Load model and dataset only once
@st.cache_resource(show_spinner=False)
def load_chatbot():
    return HealthChatbot()

st.title("🩺 AI Chatbot Kesehatan")
st.caption("Tanyakan informasi umum seputar kesehatan, penyakit, gaya hidup, dll.")

with st.spinner("Memuat model NLP (Sentence-Transformers)... Mohon tunggu sebentar."):
    chatbot = load_chatbot()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add initial greeting
    st.session_state.messages.append({"role": "assistant", "content": "Halo! Saya adalah Chatbot Asisten Kesehatan Anda. Ada yang bisa saya bantu hari ini?"})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ketik pertanyaan kesehatan Anda di sini..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response
    response = chatbot.get_response(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # Simulate stream of response with milliseconds delay
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
