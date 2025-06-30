from PyPDF2 import PdfReader
from docx import Document
import os
from typing import Optional


def get_pdf_text(pdf_file) -> str:
    '''Extracts text from each page of PDF file and combines it into one string'''
    try:
        pdf = PdfReader(pdf_file)
        all_text = []

        # Get text from each page
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                all_text.append(page_text)

        return "\n".join(all_text)

    except Exception as err:
        print(f"Error reading PDF: {err}")
        return ""


def get_docx_text(docx_file) -> str:
    """Extraxts text from DOCX file"""
    try:
        temp_file = "temp.docx"
        with open(temp_file, "wb") as f:
            f.write(docx_file.read())

        doc = Document(temp_file)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)

        os.remove(temp_file)
        return "\n".join(text)

    except Exception as e:
        st.error(f"Error reading DOCX: {e}")
        return ""


def extract_file_text(file) -> Optional[str]:
    """Checks file type and extracts its text content"""
    if file.name.endswith('.pdf'):
        return get_pdf_text(file)
    elif file.name.endswith(('.doc', '.docx')):
        return get_docx_text(file)
    elif file.name.endswith('.txt'):
        return file.read().decode("utf-8")
    else:
        st.error("File format not supported")
        return None