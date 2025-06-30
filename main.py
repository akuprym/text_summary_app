import streamlit as st
from app.interface import setup_interface
from core.summarizer import setup_model
from utils.file_handler import extract_file_text
from core.text_processor import clean_text, split_text
from core.summarizer import create_summary
from utils.config import TOKENS_LIMIT


def main():
    setup_interface()
    # Load the model
    try:
        tokenizer, summarizer = setup_model()
    except Exception as err:
        st.error(f"Error loading the model: {err}")
        return

    input_type = st.radio("Choose input type:", ("Text", "File"))

    text_for_summary = ""
    if input_type == "Text":
        text_for_summary = st.text_area("Paste your tex here:", height=250)
    else:
        uploaded_file = st.file_uploader("Upload file", type=["txt", "pdf", "docx"])
        if uploaded_file:
            with st.spinner("Processing text..."):
                text_for_summary = extract_file_text(uploaded_file)

    # Button generate summary
    if st.button("Generate Summary") and text_for_summary:
        with st.spinner("Working on it..."):

            cleaned_text = clean_text(text_for_summary)
            chunks = split_text(cleaned_text, tokenizer)

            # Progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()

            # Chunks processing
            summaries = []
            for i, chunk in enumerate(chunks):
                status_text.text(f"Processing part {i + 1} of {len(chunks)}")
                summary = create_summary(chunk, summarizer)
                summaries.append(summary)
                progress_bar.progress((i + 1) / len(chunks))

            # Create final summary
            if len(summaries) > 1:
                status_text.text("Putting it all together...")
                combined = " ".join(summaries)
                if len(tokenizer.tokenize(combined)) > TOKENS_LIMIT:
                    final_summary = create_summary(combined[:TOKENS_LIMIT * 4], summarizer)
                else:
                    final_summary = create_summary(combined, summarizer)
            else:
                final_summary = summaries[0]

            st.subheader("Here is your summary:")
            st.write(final_summary)

            st.download_button(
                label="Download summary",
                data=final_summary,
                file_name="summary.txt",
                mime="text/plain"
            )


if __name__ == "__main__":
    main()