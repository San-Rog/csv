import streamlit as st
import subprocess
import os
import pymupdf

uploadPdf = st.file_uploader('Selecionar arquivos PDF', 
                                     type=['pdf'], 
                                     accept_multiple_files=False)
if uploadPdf is not None:
    pdfName = uploadPdf.name
    docPdf = pymupdf.open(stream=uploadPdf.read(), filetype="pdf")
    command = [
                "gswin64c",  
                "-sDEVICE=pdfwrite",
                "-dCompatibilityLevel=1.4",
                f"-dPDFSETTINGS={200}",
                "-dNOPAUSE",
                "-dBATCH",
                "-sOutputFile=" + 'novo.pdf',
                docPdf
            ]
    subprocess.run(command, check=True)



