# Utiliser une image minimale
FROM python:3.12-slim

# Configuration de l'environnement
WORKDIR /app

# Installation des dépendances système
#RUN apk add --no-cache gcc musl-dev libffi-dev make

# Copie des fichiers nécessaires
COPY ./requirements.txt /app

# Installation des dépendances Python
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Copie du code de l'application
COPY ./ /app

# Exposition du port
EXPOSE 8000

# Lancement de l'application
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000", "--reload"]

