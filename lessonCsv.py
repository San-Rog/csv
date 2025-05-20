import streamlit as st

testeOne = st.button('Início')

with open('teste.css') as f:
    css = f.read()

html = """
<hmtl>
  <head>
    <h3>Meu primeiro exemplo</h3>
    <h4>Meu primeiro exemplo</h4>
    <h5>Meu primeiro exemplo</h5>
  </head>
  <body>
    <p class="center">This paragraph refers to two classes.</p>
    <p id="para1">Hello World - SOFREMOS TODAS AS DORES DO MUNDO!</p>
    <h1>My First CSS Example</h1>
    <p>Sempre ganharemos a batalha.</p>
  </body>
</html>
"""
st.write([2, 4, 5])
st.button('teste')
st.markdown(html, unsafe_allow_html=True)
#Maneiras de inserir CSS externo no streamlit.
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
#st.markdown("<link rel='stylesheet'" "href={css}>", unsafe_allow_html=True)
