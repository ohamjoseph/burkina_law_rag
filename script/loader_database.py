import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend import embeddings
from loguru import logger

from dotenv import load_dotenv

load_dotenv()

VECTOR_DIRECTORY=os.getenv("VECTOR_DIRECTORY")
FILES_DIRECTORY=os.getenv("FILES_DIRECTORY")

#Chargement d'un fichier

@logger.catch(level='ERROR')
def load_files(directory):
    logger.info("Loading files...")
    loader = DirectoryLoader(directory, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    logger.info("Loaded %d documents.", len(documents))
    return documents

def split_documents(documents):
    """
    split documents
    :param documents:
    :return:
    """

    logger.info("Splitting documents...")

    spliter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    chunks = spliter.split_documents(documents)

    logger.info("Splitted %d chunks.", len(chunks))
    return chunks


def store_documents(chunks, vectore_directory, embeddings):
    logger.info("Storing documents...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    logger.info("Save vector database in local")
    vectorstore.save_local(vectore_directory)
    logger.info("Saved vector database in local")
    logger.info("Storing documents...")


if __name__ == "__main__":
    documents = load_files(FILES_DIRECTORY)
    chunks = split_documents(documents)
    store_documents(chunks, VECTOR_DIRECTORY, embeddings.embeddings)









