# PDF Splitter API

Une API FastAPI pour découper automatiquement des PDFs à chaque occurrence de "édité le".

## 🚀 Fonctionnalités

- Découpe automatique des PDFs basée sur le texte "édité le"
- Retour des PDFs découpés en base64
- API REST simple et rapide
- Déploiement facile sur Render

## 📁 Structure du projet

```
pdf-splitter-api/
├── app.py              # API FastAPI principale
├── requirements.txt    # Dépendances Python
├── .gitignore         # Fichiers à ignorer par Git
└── README.md          # Documentation
```

## 🛠 Installation locale

1. Clonez le repository :
```bash
git clone https://github.com/votre-utilisateur/pdf-splitter-api.git
cd pdf-splitter-api
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancez l'API :
```bash
uvicorn app:app --reload
```

L'API sera disponible sur `http://localhost:8000`

## 📡 Utilisation de l'API

### Endpoint : POST `/split`

Découpe un PDF en plusieurs parties basées sur le texte "édité le".

**Paramètres :**
- `file` : Fichier PDF à découper (multipart/form-data)

**Réponse :**
```json
[
  {
    "fileName": "bilan_1.pdf",
    "data": "base64_encoded_pdf_data"
  },
  {
    "fileName": "bilan_2.pdf", 
    "data": "base64_encoded_pdf_data"
  }
]
```

**Exemple avec curl :**
```bash
curl -X POST "http://localhost:8000/split" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@votre_fichier.pdf"
```

## 🚀 Déploiement sur Render

### 1. Publier sur GitHub

```bash
# Initialiser Git
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/votre-utilisateur/pdf-splitter-api.git
git push -u origin main
```

### 2. Configuration Render

1. Allez sur [render.com](https://render.com)
2. Cliquez sur **New > Web Service**
3. Connectez votre repository GitHub
4. Configurez le service :

   - **Environment** : Python 3
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `uvicorn app:app --host 0.0.0.0 --port 10000`
   - **Port** : 10000

5. Cliquez sur **Create Web Service**

Votre API sera disponible sur une URL comme : `https://pdf-splitter.onrender.com/split`

## 🔧 Dépendances

- **FastAPI** : Framework web moderne et rapide
- **Uvicorn** : Serveur ASGI pour FastAPI
- **PyPDF2** : Bibliothèque pour manipuler les PDFs

## 📝 Notes

- L'API découpe le PDF à chaque occurrence de "édité le" (insensible à la casse)
- Les fichiers découpés sont nommés `bilan_1.pdf`, `bilan_2.pdf`, etc.
- Les PDFs sont retournés encodés en base64 pour faciliter le transfert
- L'API gère automatiquement les cas où le texte de découpe n'est pas trouvé

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.
