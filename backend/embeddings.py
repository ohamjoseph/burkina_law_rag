import os
from dotenv import load_dotenv

load_dotenv()


from langchain_ollama import OllamaLLM, OllamaEmbeddings

model = OllamaLLM(
	base_url=os.getenv("BASE_URL", "http://localhost:11434"),
	model=os.getenv('MODEL', 'llama3.2'),
	temperature=0,
)

from langchain_ollama import ChatOllama

llm = ChatOllama(
	base_url=os.getenv("BASE_URL"),
	model=os.getenv('MODEL'),
	temperature=0,
	system_prompt=(
		"Vous êtes un assistant juridique expert en droit constitutionnel du Burkina Faso. "
		"Si la question nécessite des informations spécifiques extraites de la Constitution, "
		"utilisez l'outil de recherche pour obtenir des articles pertinents."
		"Sinon comporte toi comment un chabot normal."
	)
)

embeddings = OllamaEmbeddings(
	base_url=os.getenv("BASE_URL"),
	model=os.getenv('MODEL')
)