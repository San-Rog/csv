import streamlit as st
import subprocess
import os

uploadPdf = st.file_uploader('Selecionar arquivos PDF', 
                                     type=['pdf'], 
                                     accept_multiple_files=False)
if uploadPdf is not None:
    pdfName = uploadPdf.name
    command = [
                "gswin64c",  
                "-sDEVICE=pdfwrite",
                "-dCompatibilityLevel=1.4",
                f"-dPDFSETTINGS={200}",
                "-dNOPAUSE",
                "-dBATCH",
                "-sOutputFile=" + 'novo.pdf',
                pdfName
            ]
    subprocess.run(command, check=True)

