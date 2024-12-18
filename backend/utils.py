
import os

template_str = """
    Tu es un assistant qui répond aux questions en te basant sur le contexte fourni.

    Donne une réponse en te basant sur le contexte. Si tu n'as pas de réponse à la question, réponds "Je n'ai pas de réponse à cette question".

    Sois le plus concis possible et va à l'essentiel. Et donne des reponse correcte.


    Contexte: {context}

    Question: {question}
    
    """


def ensure_directory_exists(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)
