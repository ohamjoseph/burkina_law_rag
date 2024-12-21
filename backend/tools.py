from langchain_core.tools import tool

from retrieval import retrieval
from generate_response import generate_response, index


@tool
def search_constitution_tool(query:str) -> str:
    """ Search constitution tool"""

    return retrieval(index, query)


