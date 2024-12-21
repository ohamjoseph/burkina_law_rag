from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from generate_response import generate_response, generate_stream_response

app = FastAPI()



@app.get("/generate/")
def get_generate_response(query:str):
    """
        Endpoint API pour générer une réponse via un paramètre de requête.
    """
    return  generate_response(query)

@app.get("/generate_stream/")
async def get_generate_stream_response(query: str):
    """
        Endpoint API pour générer une réponse via un paramètre de requête.
    """
    stream = generate_stream_response(query)
    return  StreamingResponse(stream, media_type='text/event-stream')