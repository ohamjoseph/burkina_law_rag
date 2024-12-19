import os
from dotenv import load_dotenv

load_dotenv()


from langchain_ollama import OllamaLLM, OllamaEmbeddings

model = OllamaLLM(
	base_url=os.getenv("BASE_URL"),
	model=os.getenv('MODEL'),
	temperature=0,
)

embeddings = OllamaEmbeddings(
	base_url=os.getenv("BASE_URL"),
	model=os.getenv('MODEL')
)