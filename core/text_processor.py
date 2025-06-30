import re
from typing import List
from utils.config import TOKENS_LIMIT, CHUNK_OVERLAP


def clean_text(text: str) -> str:
    """Cleans up messy text by:
    - Removing extra spaces
    - Fixing too many newlines
    - Removing whitespace
    """
    text = re.sub(r'\s+', ' ', text) # replace multiple spaces with 1 space
    text = re.sub(r'\n{3,}', '\n\n', text)  # replace 3+ newlines with 2
    return text.strip()  # remove spaces at the beginning/end of text


def split_text(text: str, tokenizer) -> List[str]:
    """Text splitter that:
    - Breaks long texts into manageable chunks
    - Keeps some overlap between chunks
    - Makes sure no split is too big
    """
    tokens = tokenizer.tokenize(text)
    # If text is short, return as is
    if len(tokens) <= TOKENS_LIMIT:
        return [text]

    chunks = []
    curr_chunk = []
    text_length = 0

    for token in tokens:
        curr_chunk.append(token)
        text_length += 1

        # When the limit is reached, convert tokens back to text
        if text_length >= TOKENS_LIMIT - CHUNK_OVERLAP:
            chunk_text = tokenizer.convert_tokens_to_string(curr_chunk)
            chunks.append(chunk_text)
            curr_chunk = curr_chunk[-CHUNK_OVERLAP:] if CHUNK_OVERLAP > 0 else []
            text_length = len(curr_chunk)

    # Add the last chunk if any
    if curr_chunk:
        chunks.append(tokenizer.convert_tokens_to_string(curr_chunk))

    # print(f"Split into {len(chunks)} chunks")
    # for i, chunk in enumerate(chunks):
    #     print(f"Chunk {i+1} length: {len(tokenizer.tokenize(chunk))}")

    return chunks