import streamlit as st

st.title("Crise Convulsiva na Pediatria 🧠")

st.markdown("<br>", unsafe_allow_html=True)
st.write("## Aula Comentada")

st.audio('audios/exemplo_audio.mp3')

st.divider()
st.write("## Resumo da Aula")

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Baixar Resumo da Aula",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

st.divider()
st.write("## Flashcards")

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Baixar Flashcards",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

st.divider()
st.write("## Checklist")

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Baixar Checklist",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )