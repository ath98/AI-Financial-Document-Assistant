import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores.faiss import FAISS
import getpass

# Prompt the user for the API key if it's not already set as an environment variable.
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Please enter your OpenAI API key: ")

def create_vector_store(file_path: str):
    """
    Generates a FAISS vector store for a given file. Supports only specific file types.

    Args:
        file_path (str): Path to the file for which the vector store needs to be created.

    Returns:
        FAISS: A FAISS vector store object, or None if the file type is unsupported.
    """
    # Extract file name and extension
    base_name, extension = os.path.splitext(file_path)

    # Initialize the embedding model
    embeddings = OpenAIEmbeddings()

    # Define the FAISS index storage location
    index_location = f"vector_store_{base_name}"

    # Load document based on its extension
    if extension.lower() == ".pdf":
        document_loader = PyPDFLoader(file_path=file_path)
    else:
        print("Unsupported file format. Currently, only PDF files are handled.")
        return None

    # Read and process the document
    document_content = document_loader.load()

    # Configure text splitting parameters
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,  # Increased chunk size to handle large documents more efficiently
        chunk_overlap=100,  # Adjust overlap to balance context and performance
        separators=["\n", "\n\n", "(?<=\. )", "", " "]
    )
    split_documents = splitter.split_documents(documents=document_content)

    # Generate a FAISS vector store from the processed chunks
    vector_store = FAISS.from_documents(split_documents, embeddings)

    # Save the vector store locally
    vector_store.save_local(index_location)

    return vector_store


def query_vector_store(vector_store, user_query: str) -> str:
    """
    Executes a query on a given FAISS vector store using an OpenAI language model.

    Args:
        vector_store (FAISS): The vector store to query.
        user_query (str): The query string to process.

    Returns:
        str: The response generated by the language model.
    """
    # Set up the OpenAI chat model with specific parameters
    chat_model = ChatOpenAI(temperature=0.0, verbose=True)

    # Create a RetrievalQA pipeline
    retriever_pipeline = RetrievalQA.from_chain_type(
        llm=chat_model,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )

    # Get the model's response to the query
    response = retriever_pipeline.run(user_query)

    return response
