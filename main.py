import streamlit as st
import openai

st.set_page_config(page_title="Synapso", page_icon="🧠")

st.title("🧠 Synapso – Ton IA personnelle")
st.markdown("Pose-moi une question, je te réponds intelligemment.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

prompt = st.text_area("💬 Pose ta question ici")

if st.button("Envoyer") and prompt:
    with st.spinner("Synapso réfléchit..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.markdown("### 🤖 Réponse de Synapso")
        st.write(response.choices[0].message.content)
