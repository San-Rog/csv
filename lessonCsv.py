import streamlit as st

with open('teste.css') as f:
    css = f.read()

html = """
<hmtl>
  <body>
    <p class="center">This paragraph refers to two classes.</p>
    <p id="para1">Hello World - SOFREMOS TODAS AS DORES DO MUNDO!</p>
    <h1>My First CSS Example</h1>
    <p>Sempre ganharemos a batalha.</p>
    <h3>My First CSS Example - H3</h3>
    <h4>My First CSS Example - H$</h4>
    <h5>My First CSS Example - H5</h5>
  </body>
</html>
"""
st.markdown(html, unsafe_allow_html=True)
#Maneiras de inserir CSS externo no streamlit.
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
#st.markdown("<link rel='stylesheet'" "href={css}>", unsafe_allow_html=True)