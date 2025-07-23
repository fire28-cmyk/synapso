import streamlit as st
import openai

# Configuration de la page
st.set_page_config(page_title="Synapso – Ton IA personnelle", page_icon="🧠", layout="centered")

# Chargement de la clé API
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Titre stylisé
st.markdown(
    """
    <h1 style='text-align: center; color: #4A90E2;'>🧠 Synapso</h1>
    <p style='text-align: center; font-size: 20px;'>Pose-moi une question, je te réponds intelligemment !</p>
    """,
    unsafe_allow_html=True
)

# Zone de saisie utilisateur
prompt = st.text_input("💬 Entre ta question ici :", "")

# Bouton pour envoyer la question
if st.button("✨ Envoyer"):
    if prompt.strip() == "":
        st.warning("Merci de poser une question.")
    else:
        try:
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tu es un assistant IA professionnel, aimable et clair."},
                    {"role": "user", "content": prompt}
                ]
            )
            answer = response.choices[0].message.content.strip()
            st.markdown(
                f"""
                <div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #4A90E2;'>
                    <strong>🤖 Réponse :</strong><br>{answer}
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Une erreur est survenue : {str(e)}")
