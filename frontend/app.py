import os
import time
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8000")

# Configuration de l'application Streamlit
st.set_page_config(
    page_title="Constitution du Burkina Faso - RAG",
    page_icon="📜",
    layout="centered",
    initial_sidebar_state="auto",
)

# En-tête de l'application
st.title("📜 Recherche Augmentée - Constitution du Burkina Faso")
st.write("Interrogez la Constitution à l'aide d'un modèle d'IA.")

# Streamed response emulator
def response_generator(query):
    response = requests.post(f"{API_URL}/generate/", json={"query": query})
    result = response.json()

    for line in result.splitlines():  # Divise par lignes pour respecter les retours à la ligne
        for word in line.split():  # Divise par mots pour affichage progressif
            yield word + " "
            time.sleep(0.05)
        yield "\n"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):

        response_text = ""
        placeholder = st.empty()  # Create a placeholder for incremental updates

        for chunk in response_generator(prompt):
            response_text += chunk
            placeholder.markdown(response_text)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})

st.sidebar.info("Développé par Hamed J. Ouily - Projet RAG")

