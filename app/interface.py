import streamlit as st


def setup_interface():
    # Page configuration
    st.set_page_config(
        page_title="Summary of Your Text",
        layout="wide"
    )

    st.title("Summary of Your Text")
    st.markdown("""
    ### Supported formats:
    - Text files (.txt)
    - PDF documents (.pdf)
    - Word documents (.doc, .docx)
    """)