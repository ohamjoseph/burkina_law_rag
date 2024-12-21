# from langchain.agents import initialize_agent, AgentType, create_react_agent
# from langchain.tools import Tool
#
# from embeddings import model
# from tools import search_constitution_tool
#
# tools = [
#     Tool(
#         name="RechercheConstitution",
#         func=search_constitution_tool,
#         description="Utilisez cet outil si la question fait référence à la Constitution du Burkina Faso."
#     )
# ]
#
# # agent = initialize_agent(
# #     llm=model,
# #     tools=tools,
# #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# #     verbose=True
# # )
# from langchain_core.prompts import PromptTemplate
# prompts = """Tu est Alvine une assistante pour repondre aux questions sur les texte de loi du burkina
#            Pour pouvoir reponde au mieux aux questions sur le constitution du Burkina Faso utilise {tools} pour enrichire ton contexte.
#            Question: {input}
#             Thought:{agent_scratchpad}'''
#            """
#
#
# prompt = PromptTemplate.from_template(prompts)
# agent=create_react_agent(
#     tools=[search_constitution_tool],
#     llm=model,
#     prompt=prompt,
#     verbose=True,
#
# )
#
#
# agent.invoke("Bonjour")
from typing import Annotated

from langgraph.graph import StateGraph, START, END
from langgraph.graph import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict

from tools import search_constitution_tool
from embeddings import model,llm


class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

tools = [search_constitution_tool]

llm_with_tools = llm.bind_tools(tools)



def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

tool_node = ToolNode(tools=tools)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_node('tools', tool_node)

# Condition Personnalisée
def is_constitution_related(state: str):
    """ Vérifie si la question concerne la Constitution. """

    print(model.invoke(f"Analyse le texte suivant et détermine s'il s'agit d'une question portant sur la Constitution du Burkina Faso. " 
f"Réponds uniquement par 'oui' ou 'non'.\nTexte : {state}"

                       ))

    # last_message = state["messages"][0].content.lower()  # Texte du dernier message utilisateur
    # keywords = ["constitution", "article", "loi", "droit"]
    # return "tools" if keywords in last_message else "END"


is_constitution_related("Qu'est ce que la constitution ?")

# graph_builder.add_conditional_edges(
#     'chatbot',
#         is_constitution_related,
#     {"tools":"tools", "END":END}
# )
#
#
#
# graph_builder.add_edge('tools',"chatbot")
# graph_builder.set_entry_point('chatbot')
#
# graph = graph_builder.compile(debug=True)
#
# user_input = "Bonjour"
# def stream_graph_updates(user_input: str):
#     for event in graph.stream({"messages": [("user", user_input)]}):
#
#         for value in event.values():
#             print("Assistant:", value["messages"][-1])
#
# stream_graph_updates(user_input)
