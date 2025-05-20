import streamlit as st

st.write([2, 4, 5])
colOne, colTwo = st.columns(2)
with colOne:
    st.text('colOne')
    st.button('Início')
    st.selectbox('Escolha One', [0, 1, 2, 4])    
with colTwo: 
    st.text('colTwo')
    st.button('Fim')
    st.selectbox('Escolha One', [0, 1, 2, 4]) 
with open('teste.css') as f:
    css = f.read()

html = f"""
<hmtl>
  <head>
    <h3>Meu primeiro exemplo</h3>
    <h4>Meu primeiro exemplo</h4>
    <h5>Meu primeiro exemplo</h5>
  </head>
  <body>
    <p class="center">This paragraph refers to two classes.</p>
    <p class="img">Imagem de fundo sdfsdfsdfsdfsdfsdf.</p>
    <p id="para1">Hello World - SOFREMOS TODAS AS DORES DO MUNDO!</p>
    <h1>My First CSS Example</h1>
    <p>Sempre ganharemos a batalha.</p>
  </body>
</html>
"""
st.markdown(html, unsafe_allow_html=True)
#Maneiras de inserir CSS externo no streamlit.
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
#st.markdown("<link rel='stylesheet'" "href={css}>", unsafe_allow_html=True)
