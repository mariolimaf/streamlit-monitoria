import streamlit as st

st.title("Semiologia do Aparelho Digestório 💩")

st.markdown("<br>", unsafe_allow_html=True)
st.write("## Aula Comentada")

st.write("#### Apendicite")
st.audio('audios/exemplo_audio.mp3')

st.write("#### Mononucleose Infecciosa")
st.audio('audios/exemplo_audio.mp3')

st.write("#### Intussuscepção Intestinal")
st.audio('audios/exemplo_audio.mp3')

st.divider()
st.write("## Resumos das Aulas")
st.write("##### PDF de resumo para cada aula")

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Resumo - Apendicite",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Resumo - Mononucleose Infecciosa",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Resumo - Intussuscepção Intestinal",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

st.divider()
st.write("## Flashcards")

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Flashcards - Apendicite",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Flashcards - Mononucleose Infecciosa",
        data=f,
        file_name="Aula_SBV.pdf",
        mime="application/pdf"
    )

with open('pdfs/aula_teste.pdf', "rb") as f:
    st.download_button(
        label="📥 Flashcards - Intussuscepção Intestinal",
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