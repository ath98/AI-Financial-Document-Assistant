# Use the official Python Alpine base image
FROM ubuntu/python:3.12-24.04_stable

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies required for Streamlit and other libraries
RUN apt-get install \
    gcc \
    g++ \
    make \
    libffi-dev \
    openssl-dev \
    swig \
    libgomp \
    && rm -rf /var/cache/apk/*

# Copy the requirements file into the container
#COPY requirements.txt /app/requirements.txt



# Copy the application code into the container
COPY . /app
# Install Python dependencies
RUN pip install -r /app/requirements.txt

# Expose the default Streamlit port
EXPOSE 8501

# Set Streamlit configuration options
ENV STREAMLIT_SERVER_PORT 8501
ENV STREAMLIT_SERVER_ADDRESS 0.0.0.0

# Set the entrypoint to run the Streamlit app
ENTRYPOINT ["streamlit", "run"]

# Specify the main application file
CMD ["chatbot_app.py"]
