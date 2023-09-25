## Foires aux questions

Ceci est une proposition d'application pour gérer une application de "FAQ" 

## Fonctionnalités 

- Les visiteurs peuvent poser des questions
- Le client peut visualiser la liste des questions et y répondre
- Les visiteurs peuvent consulter la FAQ (qui est la liste des questions ayant obtenu une réponse)
- L'application doit être réalisé avec le framework Django

## Démarrage du projet localement

## Installation des paquets nécessaires

### Frontend
- Dans la racine du projet lancer : npm install

### Backend
 - Dans la racine du projet , créer un 'virtual env' :  python3 -m venv venv
 - Activer le venv : source venv/bin/activate
 - Installer les paquets dans src/requirements.txt :   pip install -r src/requirements.txt

### Base de données
 - Le projet utilse PostgresSQL
 - Avant de lancer la migration, il faut d'abord créer la BDD localement selon le nom configué dans la variable défini dans le fichier settings.py
 - Une fois la base créé, aller dans le répertoire src/QuestionBox/ puis lancer la commande : python manage.py migrate

### Démarrage du serveur 
  - Aller dans le répertoire src
  - Lancer la commande : python3.11 manage.py runserver
  - Dans un autre terminal, dans la racine du projet lancer la commande :  npm run dev

## Déploiement
## Test
## CI/CD
