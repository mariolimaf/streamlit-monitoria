import streamlit as st

st.title("Suporte Básico de Vida e Engasgo na Criança e no Adolescente 🚨")

st.markdown("<br>", unsafe_allow_html=True)
st.write("## Aula Comentada")

st.write("#### SBV")
st.audio('audios/exemplo_audio.mp3')

st.write("#### Engasgo")
st.audio('audios/exemplo_audio.mp3')

st.divider()
st.write("## Resumos das Aulas")
st.write("##### PDF de resumo para cada aula")

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Resumo - SBV",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Resumo - Engasgo",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

st.divider()
st.write("## Flashcards")

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Flashcards - SBV",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Flashcards - Engasgo",
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