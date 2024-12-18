# 📜 **Application de Recherche Augmentée - Constitution du Burkina Faso**  

Une application basée sur l'intelligence artificielle utilisant LangChain et Ollama pour effectuer une recherche augmentée dans la Constitution du Burkina Faso. Elle comprend un backend API développé avec FastAPI et une interface utilisateur construite avec Streamlit.

---

## **🚀 Déploiement Local**

### **1. Prérequis**  
- **Python 3.9+**  
- **Docker (facultatif)**  

### **2. Installation**
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-compte/burkina_law_rag.git
   cd burkina_law_rag
   ```

2. Créez et activez l'environnement virtuel :
   ```bash
   python -m venv rag_env
   source rag_env/bin/activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Configurez les variables d'environnement :
   ```bash
   cp .env.example .env
   ```

---

### **3. Installation de Ollama et LLaMA3.2**  

#### **3.1. Installation d’Ollama**
1. **Téléchargez Ollama** :  
   Suivez les instructions d’installation officielles sur le site d’Ollama :  
   [Installation d'Ollama](https://ollama.com/download)

2. **Lancez Ollama Localement** :
   ```bash
   ollama serve --host localhost --port 11434
   ```

---

#### **3.2. Installation de LLaMA 3.2**
1. **Téléchargement du Modèle LLaMA 3.2**
   ```bash
   ollama pull llama3.2
   ```

2. **Vérification du Modèle** :
   ```bash
   ollama list
   ```

3. **Ajoutez LLaMA à vos Variables d’Environnement** :
   ```env
   MODEL=llama3.2
   OLLAMA_HOST=http://localhost:11434
   ```

---

### **4. Lancement de l'API Backend (FastAPI)**
```bash
fastapi dev backend/main.py
```

---

### **5. Lancement de l'Interface Utilisateur (Streamlit)**
```bash
streamlit run frontend/app.py
```

---

### **6. Accès à l'Application**
- **Backend API** : [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger)  
- **Frontend Streamlit** : [http://localhost:8501](http://localhost:8501)

---

## **🔧 Utilisation avec Docker**
Si vous préférez Docker, utilisez `docker-compose` :  

```bash
docker-compose up --build
```

---

## **📊 Fonctionnalités**
1. **Recherche Augmentée :** Interrogez la Constitution avec des requêtes en langage naturel.  
2. **Modèle IA Local :** Utilise LLaMA en local via Ollama.  
3. **Backend API REST :** Développé avec FastAPI, documentation incluse.  
4. **Interface Utilisateur Simple :** Streamlit pour une expérience utilisateur fluide.  

---

## **📦 Technologies Utilisées**
- **Langues :** Python 3.9+  
- **Frameworks Backend :** FastAPI, FAISS  
- **Frontend :** Streamlit  
- **IA & Modèles :** LangChain, Ollama, LLaMA  

---

## **🔒 Sécurité et Confidentialité**
- Les clés API et configurations sont stockées dans `.env`.  
- **Important :** Ne partagez pas ce fichier `.env` en public.

---

## **📄 Licence**
Ce projet est sous licence **MIT**.

---
