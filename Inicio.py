import streamlit as st

st.set_page_config(
    page_title='Monitoria'
)

"# Bem vindos a Monitoria de CHA V - Pediatria! 👶"

st.page_link("pages/1_Semiologia Respiratória.py", label="Semiologia Respiratória", icon='➖')
st.page_link("pages/2_Semiologia do Aparelho Digestório.py", label="Semiologia do Aparelho Digestório", icon='➖')
st.page_link("pages/3_SBV e Engasgo.py", label="SBV e Engasgo", icon='➖')
st.page_link("pages/4_Crise Convulsiva na Pediatria.py", label="Crise Convulsiva na Pediatria", icon='➖')
st.page_link("pages/5_Consulta do Adolescente.py", label="Consulta do Adolescente", icon='➖')
st.page_link("pages/6_Plantão Tira Dúvidas.py", label="Plantão Tira Dúvidas", icon='➖')
st.page_link("pages/7_Dúvidas Frequentes.py", label="Dúvidas Frequentes", icon='➖')
