# Text Summarization with BART

A Python app for summarizing text/files using the BART model, with support for PDF, DOCX, and TXT inputs.

## Features

- **Multi-format support**: Process PDFs, Word docs, and plain text
- **Smart chunking**: Handles long documents with configurable overlap
- **Downloadable results**: Save summaries as TXT files
- **Progress tracking**: Real-time processing updates

<img width="1364" alt="Screenshot 2025-06-30 at 05 37 21" src="https://github.com/user-attachments/assets/c131a84f-ab32-4c0f-88ae-9d831808d251" />

## Installation

1. Clone the repo:
   ```
   git clone https://github.com/akuprym/text_summary_app
   cd text_summary_app
   ```

## Install requirements:
```
pip install -r requirements.txt
```

## Usage
### Web Interface
```
streamlit run main.py
```
## Why BART Model?

**Seq2Seq architecture** - Ideal for text generation tasks      
**Pretrained on CNN/DM** - Fine-tuned for summarization           
**1024-token context**  - Handles longer paragraphs than most models  
**Efficient** - Runs fast on consumer hardware

## How It Processes Long Texts
### 1. Chunking with Overlap
- Preserves context with CHUNK_OVERLAP=100 (10% of BART's limit)
- Prevents sentence fragmentation at boundaries
### 2. Hierarchical Summarization

For very long documents (>10K tokens):

- Split into chunks (with overlap)
- Summarize each chunk
- Combine chunk summaries
- Summarize the combined result
