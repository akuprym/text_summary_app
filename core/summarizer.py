from transformers import pipeline, AutoTokenizer
import streamlit as st
from utils.config import MIN_RESULT_LEN, MAX_RESULT_LEN


@st.cache_resource
def setup_model():
    # Convert words to numbers
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    # Set up model
    model = pipeline(
        "summarization",
        model="facebook/bart-large-cnn",
        tokenizer=tokenizer
    )
    return tokenizer, model


def create_summary(split: str, summarizer) -> str:
    # Summarize one split
    try:
        summary = summarizer(
            split,
            max_length=MAX_RESULT_LEN,
            min_length=MIN_RESULT_LEN,
            do_sample=False
        )
        return summary[0]['summary_text'] # return the first summary
    except Exception as e:
        st.warning(f"Error summarizing text: {e}")
        return split[:200] + "..."  # return the first 200 characters instead