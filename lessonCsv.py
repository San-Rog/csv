import streamlit as st
import subprocess
import os
import pymupdf

command = [
               "/mount/src/csv/gswin64c.exe",  
                "-sDEVICE=pdfwrite",
                "-dCompatibilityLevel=1.4",
                f"-dPDFSETTINGS={200}",
                "-dNOPAUSE",
                "-dBATCH",
                "-sOutputFile=" + 'novo.pdf',
                'file.pdf'
            ]
subprocess.run(command, check=True)








