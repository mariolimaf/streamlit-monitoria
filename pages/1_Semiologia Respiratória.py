import streamlit as st

st.title("Semiologia Respiratória 🫁")

st.write("## Aula Comentada")

st.write("#### Asma")
st.audio('audios/exemplo_audio.mp3')

st.write("#### BVA")
st.audio('audios/exemplo_audio.mp3')

st.write("#### Pneumonia")
st.audio('audios/exemplo_audio.mp3')

st.divider()
st.write("## Resumos das Aulas")
st.write("##### PDF de resumo para cada aula")

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Resumo - Asma",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/BVA MONITORIA.pdf', "rb") as f:
    st.download_button(
        label="📥 Resumo - BVA",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Resumo - Pneumonia",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

st.divider()
st.write("## Flashcards")

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Flashcards - Asma",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Flashcards - BVA",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Flashcards - Pneumonia",
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