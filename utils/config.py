# Constants for text processing
TOKENS_LIMIT = 1024  # BART model limit
CHUNK_OVERLAP = 100  # Optimal for BART:
# - Small enough to avoid redundant processing (~10% of 1024-token limit)
# - Large enough to preserve context across chunk boundaries
# - Showed the best result while testing on large and short texts
MIN_RESULT_LEN = 50
MAX_RESULT_LEN = 150