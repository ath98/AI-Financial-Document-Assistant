# AI Financial Document Assistant

This repository demonstrates an AI-powered application that allows users to query financial documents (PDFs) using natural language. The system combines modern AI technologies, including OpenAI's GPT model and FAISS, to provide accurate and efficient answers from uploaded documents.

## Features

- Upload financial or text-based PDF documents.
- Create vectorized representations of documents for efficient querying.
- Use OpenAI's language model to generate human-like responses based on document content.

## Architecture Overview

The system is built using:

- **OpenAI GPT Model**: Generates natural language responses.
- **FAISS**: Efficiently stores and retrieves vectorized document chunks.
- **Streamlit**: Provides a user-friendly interface.

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher installed.
2. OpenAI API key (required for GPT model access).
3. Required Python packages installed (see below).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/ai-financial-document-assistant.git
   cd ai-financial-document-assistant
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:

   - Open your terminal and run:
     ```bash
     export OPENAI_API_KEY="your_openai_api_key_here"
     ```
   - Alternatively, add it to your environment variables permanently.

### Running the Application

#### Using Python

1. Start the Streamlit application:

   ```bash
   streamlit run chatbot_app.py
   ```

2. Open the application in your browser using the URL provided in the terminal (usually `http://localhost:8501`).

#### Using Docker

1. Build the Docker image:

   ```bash
   docker build -t ai-financial-doc-assistant .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8501:8501 -e OPENAI_API_KEY="your_openai_api_key_here" ai-financial-doc-assistant
   ```

3. Open the application in your browser using the URL `http://localhost:8501`.

> **Note:** Ensure that you replace `your_openai_api_key_here` with your actual OpenAI API key. You can also use a `.env` file to manage environment variables.

### Using the Application

1. **Upload Document**:

   - Upload a PDF file (financial document).
   - Ensure the file is in the correct format (PDF only).

2. **Ask Questions**:

   - Enter a question in the text input box (e.g., "What is the total revenue for Q1?").
   - View the response generated by the AI model based on the document.

## Environment Variables

The following environment variables are used in the application:

- `OPENAI_API_KEY`: Your OpenAI API key for accessing GPT model capabilities.

You can set these variables directly in your terminal, or use a `.env` file with the following format:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Colab Notebook

A fully functional Colab notebook is available to demonstrate the core functionalities:

- Uploading a PDF document.
- Creating a FAISS vector store.
- Querying the document using OpenAI's GPT model.

Use the provided notebook to run the QA pipeline interactively.

## File Descriptions

- `chatbot_app.py`: Contains the Streamlit-based frontend for file uploads and querying.
- `test_api.py`: Includes core functions for creating vector stores and querying documents.
- `requirements.txt`: Lists all dependencies required to run the project.
- `Dockerfile`: Contains instructions for building a Docker image of the application.

## Future Enhancements

1. Add support for non-PDF formats (e.g., Word documents).
2. Implement multi-language support for documents and queries.
3. Integrate caching for faster repeated queries.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute, open issues, or provide feedback to improve this repository!

