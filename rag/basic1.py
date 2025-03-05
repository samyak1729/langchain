import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_cohere import CohereEmbeddings

# Define file path before using it
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "documents", "lord_of_the_rings.txt")

loader = TextLoader(file_path, encoding="latin-1")  # Change encoding

# Get your API key from environment variables (or hardcode it, but not recommended)
COHERE_API_KEY = "WRwb7tmZVzjZMhCfL9mEUROiiUBKzluoiJp4KbA5"

# Define directories
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "documents", "lord_of_the_rings.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

if not os.path.exists(persistent_directory):
    print("Initializing vector store...")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Load and split text
    loader = TextLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    # Use Cohere API for embeddings
    print("\n--- Creating embeddings with Cohere API ---")
    embeddings = CohereEmbeddings(model="embed-english-v3.0", cohere_api_key=COHERE_API_KEY)
    
    # Store embeddings in Chroma
    db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Finished creating vector store ---")
else:
    print("Vector store already exists.")

