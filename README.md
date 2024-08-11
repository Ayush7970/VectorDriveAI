
# Project Name: VectorDriveAI

## Project Overview
VectorDriveAI is an advanced document querying and indexing system that integrates Google Drive document storage with a GPT-based language model using PyTorch. This project leverages vector embeddings and PostgreSQL vector storage (pgvector) to efficiently manage and query large document datasets. The system also incorporates Ollama's embedding and language models to enhance the document processing and querying capabilities.

## Features
- **Google Drive Integration**: Authenticates with Google Drive to load and manage documents, enabling seamless integration with cloud-based storage.
- **GPT-based Language Model**: Utilizes a transformer-based language model to process and understand document content.
- **Vector Storage with PostgreSQL**: Stores document embeddings in PostgreSQL using the pgvector extension, facilitating efficient similarity searches.
- **Interactive Query Engine**: Allows users to interactively query the indexed documents and receive contextually relevant answers based on the language model's understanding.
- **Scalable Architecture**: Supports processing large datasets and handling complex queries through robust vector storage and retrieval mechanisms.

## Technical Stack
- **Programming Language**: Python
- **Machine Learning Framework**: PyTorch
- **Database**: PostgreSQL with pgvector extension
- **Cloud Storage**: Google Drive API
- **Embedding & LLM**: Ollama's GPT-based models
- **Web Framework**: Flask (if applicable)

## Installation and Setup

### Prerequisites
- Python 3.x
- PostgreSQL with pgvector extension installed
- Google Cloud project credentials for Google Drive API
- PyTorch installed in your environment

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/VectorDriveAI.git
   cd VectorDriveAI
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up PostgreSQL**:
   - Ensure PostgreSQL is installed and running.
   - Install the pgvector extension.

4. **Configure Google Drive Authentication**:
   - Place your Google OAuth credentials in the specified location.
   - Authenticate Google Drive using the provided script.

5. **Run the Project**:
   ```bash
   python main.py
   ```

## Usage
- **Document Loading**: Load documents from Google Drive using the specified file IDs.
- **Index Creation**: Create a vector store index from the loaded documents.
- **Querying**: Interactively query the documents using natural language, and receive contextually accurate responses.

## Acknowledgment 
- **This project was completed under the guidance of Professor Chris Kanich.

