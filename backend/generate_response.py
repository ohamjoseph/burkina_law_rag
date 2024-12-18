from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap

import utils
from embeddings import model
from retrieval import load_index, retrieval


parser = StrOutputParser()

prompt = PromptTemplate.from_template(utils.template_str)

path = "/home/hamed/Documents/Perso/Python/mastering_rag/embeddings_model/RAG/data/database"
index = load_index(path)

chain = (
    RunnableMap({
        "context": lambda x: retrieval(index, x["question"]),
        "question": lambda x: x["question"]
    })
    | prompt
    | model
    | parser
)

def generate_response(query):
    request = {"question": query}
    return chain.invoke(request)
