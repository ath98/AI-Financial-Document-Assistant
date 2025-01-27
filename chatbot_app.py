import streamlit as st
from test_api import query_vector_store, create_vector_store

# Set the title for the application.
st.title("AI Financial Document Assistant")

# Enable users to upload their document files.
file_upload = st.file_uploader("Upload your document (PDF only):", type=("pdf"))

# Provide an input box for the user to ask questions.
user_query = st.text_input(
    "Enter your question about the document:",
    placeholder="E.g., What are the total expenses for Q2 2023?",
    disabled=not file_upload,
)

# Process the uploaded file if provided by the user.
if file_upload:
    try:
        # Save the uploaded file temporarily.
        with open(file_upload.name, "wb") as temp_file:
            temp_file.write(file_upload.getbuffer())

        # Generate a FAISS vector store from the uploaded file.
        vector_store = create_vector_store(file_upload.name)

        # Handle unsupported file types gracefully.
        if vector_store is None:
            st.error("Unsupported file type. Please upload a PDF document.")

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")

# Display a loading spinner while processing the query.
with st.spinner("Fetching your response..."):
    if file_upload and user_query:
        try:
            # Query the vector store and fetch the response.
            response = query_vector_store(vector_store, user_query)

            # Display the answer in a clean format.
            st.markdown("### Response")
            st.write(response)

        except Exception as e:
            st.error(f"An error occurred while processing your query: {e}")

        finally:
            st.markdown("---")  # Add a divider for better UI clarity.

