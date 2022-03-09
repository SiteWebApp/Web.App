import streamlit as st

st.title("Exemplo de aplicativo web")

opções = st.selectbox("Selecione", ['Opção 1', 'Opção 2'])

x = st.slider("Escolha 0 e 10",min_value=0, max_value=10, step = 1)   