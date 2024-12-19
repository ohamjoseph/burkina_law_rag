from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from generate_response import generate_response, generate_stream_response

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/generate/")
def get_generate_response(query: QueryRequest):
    """
        Endpoint API pour générer une réponse via un paramètre de requête.
    """
    return  generate_response(query.query)

@app.get("/generate_stream/")
async def get_generate_stream_response(query: QueryRequest):
    """
        Endpoint API pour générer une réponse via un paramètre de requête.
    """
    stream = generate_stream_response(query.query)
    return  StreamingResponse(stream, media_type='text/event-stream')