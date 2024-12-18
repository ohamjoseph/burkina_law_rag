import os

from langchain_community.vectorstores import FAISS
from embeddings import embeddings



def load_index(path:str):
    if not os.path.exists(path):
        raise RuntimeError(f"Fichier introuvable : {path}")
    index = FAISS.load_local(
        path, embeddings,
        allow_dangerous_deserialization=True)
    return index


def retrieval(index, query, top_k=5):
    try:
        indices = index.similarity_search(query, top_k)
    except AttributeError:
        raise AttributeError("Index not found")

    re = [f"Source {id+1}\n : {index.page_content.strip()}" for id, index in enumerate(indices)]
    return "\n\n".join(re)


# def chain(index):