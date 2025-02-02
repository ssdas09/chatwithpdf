# Chat with Multiple PDFs using Gemini

This project allows users to upload multiple PDF files and interactively chat with their content using Google's Gemini AI. The application processes the PDFs, extracts text, stores vector embeddings, and enables users to ask questions with context-aware responses.

## Features

- Upload multiple PDF files.
- Extract and process text from PDFs.
- Store vector embeddings using FAISS.
- Interact with the content using Google Gemini AI.
- Streamlit-based user interface for seamless interaction.

## Tech Stack

- **Python**
- **Streamlit** (for UI)
- **PyPDF2** (for PDF text extraction)
- **LangChain** (for text processing and QA chain)
- **FAISS** (for vector storage and retrieval)
- **Google Generative AI** (for embeddings and chat responses)
- **Dotenv** (for managing API keys)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Add your Google Generative AI API key:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Upload PDF files from the sidebar.

3. Click "Submit & Process" to extract and store the text.

4. Ask questions based on the uploaded PDFs.

## File Structure

```
├── app.py  # Main application script
├── requirements.txt  # Dependencies
├── README.md  # Documentation
├── .env  # API keys (not to be committed)
```

## Notes

- Ensure you have a valid Google API key for embedding and chat functionalities.
- The FAISS index is stored locally for faster retrieval.

## Contributing

Feel free to fork this repository and submit pull requests!

## License

This project is licensed under the MIT License.

give me the markdown code

give 
