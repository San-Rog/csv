import streamlit as st
import subprocess
import os

# Ensure Ghostscript is installed and in PATH
def compress_pdf(input_path, output_path, quality_setting="/screen"):
    """Compresses a PDF using Ghostscript."""
    try:
        command = [
            "gswin64c",  
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS={quality_setting}",
            "-dNOPAUSE",
            "-dBATCH",
            "-sOutputFile=" + output_path,
            input_path
        ]
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        st.error(f"Error compressing PDF: {e}")
        return False

st.title("PDF Compressor with Ghostscript")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    temp_input_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(temp_input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write(f"Uploaded: {uploaded_file.name}")

    output_filename = f"compressed_{uploaded_file.name}"
    temp_output_path = os.path.join("temp", output_filename)

    if compress_pdf(temp_input_path, temp_output_path):
        st.success("PDF compressed successfully!")
        with open(temp_output_path, "rb") as f:
            st.download_button(
                label="Download Compressed PDF",
                data=f.read(),
                file_name=output_filename,
                mime="application/pdf"
            )
    
    # Clean up temporary files
    os.remove(temp_input_path)
    if os.path.exists(temp_output_path):
        os.remove(temp_output_path)
