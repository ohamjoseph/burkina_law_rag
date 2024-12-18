import os
from operator import itemgetter
from dotenv import load_dotenv
from loguru import logger

from backend.embeddings import embeddings  # Use absolute import here
from langchain_core.runnables.base import RunnableMap
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from huggingface_hub import InferenceClient

from langchain.llms.base import LLM
from typing import List
from pydantic import Field

class HuggingFaceInferenceClientLLM(LLM):
    client: InferenceClient = Field(...)

    def __init__(self, client: InferenceClient):
        super().__init__(client=client)


    @property
    def _llm_type(self) -> str:
        return "huggingface_inference_client"

    def _call(self, prompt: str, stop: List[str] = None) -> str:
        # Use the `text_generation` method, depending on the model's capability
        response = self.client.text_generation(prompt)  # Adjust method if needed
        return response



# Load environment variables
load_dotenv()

VECTOR_DIRECTORY = os.getenv("VECTOR_DIRECTORY")
HF_API_KEY = os.getenv("HF_API_KEY")



client = InferenceClient(
    api_key=HF_API_KEY,
    model="microsoft/Phi-3.5-mini-instruct"
)

# print(client.text_generation("Bonjour Comment tu vas?"))


hf_llm = HuggingFaceInferenceClientLLM(client=client)

# Test with a prompt
prompt = "Bonsoir Comment tu vas ?"
response = hf_llm.invoke(prompt)
print(response)

def chat_chain():

    template_str = """
    Tu es un assistant qui répond aux questions en te basant sur le contexte fourni.

    S'il te plait, donne une réponse en te basant sur le contexte. Si tu n'as pas de réponse à la question, réponds "Je n'ai pas de réponse à cette question".

    Sois le plus concis et explicite possible. Et donne des reponse correcte.


    Contexte: {context}

    Question: {question}
    """

    # Load and initialize components
    prompt = PromptTemplate.from_template(template_str)
    recuperation = FAISS.load_local("/home/hamed/Documents/Perso/Python/mastering_rag/embeddings_model/RAG/data/database", embeddings, allow_dangerous_deserialization=True)
    model = ChatOllama(
        model=os.getenv("MODEL"), temperature=0
    )
    parser = StrOutputParser()

    logger.info("Prompt, FAISS, ChatOllama model, and StrOutputParser initialized successfully.")
    print(recuperation.similarity_search("Quels sont les droits du burkinabè "))
    # Define the chain with RunnableMap and appropriate callables
    chain = (
        RunnableMap({
            "context": lambda x: recuperation.similarity_search(itemgetter("question")(x)),
            "question": lambda x: itemgetter("question")(x)
        })
        | prompt
        | hf_llm
        | parser
    )

    logger.info("Chain constructed successfully.")

    return chain

chain = chat_chain()

print(chain.invoke({"question": "Quels sont les rôles du president de la republique ?"}))
