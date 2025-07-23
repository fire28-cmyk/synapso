import streamlit as st
from openai import OpenAI

# Titre de l'appli
st.title("🧠 Synapso – Ton IA personnelle")
st.write("Pose-moi une question, je te réponds intelligemment.")

# Champ pour entrer la question
prompt = st.text_input("Ta question ici...")

# Si l'utilisateur écrit une question
if prompt:
    # Initialisation du client OpenAI avec ta clé API
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Envoie de la requête à GPT
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    # Récupération et affichage de la réponse
    reply = response.choices[0].message.content
    st.write("🤖 Réponse :", reply)
