

# Chat PDF using Gemini💁

This Streamlit application allows users to chat with a PDF document using the Gemini conversational AI model. Before starting the conversation, users need to upload a CSV, PDF, or TXT file containing the context from which queries will be answered.


## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.6+
- Streamlit
- PyPDF2
- langchain
- langchain_google_genai
- FAISS
- dotenv

### Installation

Clone this repository:

```bash
git clone https://github.com/chuck-ankit/LLM/tree/main/Learning/Langchain
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

Run the Streamlit app:

```bash
streamlit run app.py
```

### Usage

1. Upload your files containing the context from which queries will be answered. You can upload CSV, PDF, or TXT files.
2. Click on the "Submit & Process" button to process the uploaded files.
3. Ask your questions in the text input field provided.
4. The application will generate responses based on the provided context from the uploaded files.

## Implementation Details

- **File Formats**: Supported file formats for context include CSV, PDF, and TXT.
- **Text Extraction**: Text is extracted from uploaded files using PyPDF2 for PDFs, standard file reading for TXT files, and CSV reading for CSV files.
- **Text Chunking**: Text is split into chunks for efficient processing.
- **Vectorization**: Google Generative AI embeddings are used to vectorize text chunks.
- **Conversation Chain**: Gemini conversational AI model is used to generate responses based on the user's questions and the provided context.

## Environment Variables

- `GOOGLE_API_KEY`: API key required for Google Generative AI. Set it in a `.env` file.

---
