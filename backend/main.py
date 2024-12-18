from fastapi import FastAPI
from pydantic import BaseModel

from generate_response import generate_response

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/generate/")
def get_generate_response(query: QueryRequest):
    """
        Endpoint API pour générer une réponse via un paramètre de requête.
    """
    return  generate_response(query.query)