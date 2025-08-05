import streamlit as st
import subprocess
import os
import pymupdf

command = [
                "gswin64c",  
                "-sDEVICE=pdfwrite",
                "-dCompatibilityLevel=1.4",
                f"-dPDFSETTINGS={200}",
                "-dNOPAUSE",
                "-dBATCH",
                "-sOutputFile=" + 'novo.pdf',
                'file.pdf'
            ]
subprocess.run(command, check=True)






