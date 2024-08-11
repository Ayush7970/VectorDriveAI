import logging
import sys
from llama_index.core import VectorStoreIndex, Settings
from llama_index.readers.google import GoogleDriveReader
from google_drive_auth import authenticate_google_drive
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.readers.google import GoogleDriveReader
from llama_index.llms.ollama import Ollama
from llama_index.core.schema import MetadataMode

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

 # This loads the .env file at the application's root directory

# Authenticate Google Drive
service, client_config = authenticate_google_drive()

# Load documents from Google Drive
documents = GoogleDriveReader(
    file_ids=["enter file ids"],
    service=service,
    client_config=client_config
).load_data()

# Set up Ollama
ollama_embedding = OllamaEmbedding(
    model_name="llama3",
    base_url=" enter your base url",
    ollama_additional_kwargs={
        "mirostat": 0,
        "num_ctx": 4096,
        "num_predict": -1,
        "seed": 42,
    },
)
ollama_llm = Ollama(model="llama3", request_timeout=120.0)
Settings.embed_model = ollama_embedding
Settings.llm = ollama_llm

# Apply text template to documents
for i in range(len(documents)):
    documents[i].text_template = """-----BEGIN METADATA-----
{metadata_str}
-----END METADATA-----
-----BEGIN CONTENT-----
{content}
-----END CONTENT-----"""

# Create index from documents
# index = VectorStoreIndex.from_documents(documents, show_progress=True)
# query_engine = index.as_query_engine()

print("The LLM sees this:\n" + documents[i].get_content(metadata_mode=MetadataMode.LLM))
print("The Embedding model sees this:\n" + documents[i].get_content(metadata_mode=MetadataMode.EMBED))
print(documents[i].__repr__)

index = VectorStoreIndex.from_documents(
    documents=documents,
    show_progress=True,
)
query_engine = index.as_query_engine()
# Interactive query loop
while True:
    query = input("Query: ")
    answer = query_engine.query(query)
    print(f"Answer: {answer}")
