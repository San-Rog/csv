import streamlit as st
import os
import subprocess

st.write([2, 4, 5])
colOne, colTwo = st.columns(2)
with colOne:
    text = st.markdown("<p class='centerButt'>Botão A.</p>", unsafe_allow_html=True)
    st.button('Botão A')
    st.selectbox('Escolha One', [0, 1, 2, 4])    
    st.markdown("<a href='https://www.streamlit.io'>Site XYZ</a>", unsafe_allow_html=True)
with colTwo: 
    st.markdown("<p class='centerButt'>Botão B.</p>", unsafe_allow_html=True)
    st.button('Botão B')
    st.markdown("<p class='center'>This paragraph refers to two classes.</p>", unsafe_allow_html=True)
    st.selectbox('', [5, 6]) 
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
    <div>Divisão ocupando espaço na tela</div>
    <p class="ocup">Ocupação de espaço com altura e largura predefinidos.</p>
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
#st.write(os.getcwd())
dirNow = os.getcwd()
st.write(dirNow)
st.write(os.listdir(dirNow))
filePdf = 'teste_pdf.pdf'
newFile = 'teste_pdf.jpg'
fileGs = os.path.join(dirNow, 'gswin64c.exe')
progExe = [
        fileGs, 
        "-sDEVICE=jpeg",
        "-r300",  # Resolution
        "-o", newFile, # Output file
        filePdf # Input file
]
try:
    result = subprocess.run(
            progExe,
            capture_output=True, 
            text=True, 
            check=True)
except Exception as error:
    st.text(error)



