## Foires aux questions

Ceci est une proposition d'application pour gérer une application de "FAQ" 

## Fonctionnalités 

- Les visiteurs peuvent poser des questions
- Le client peut visualiser la liste des questions et y répondre
- Les visiteurs peuvent consulter la FAQ (qui est la liste des questions ayant obtenu une réponse)
- Une api pour au moins récupérer la liste des questions 
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
 - Créer un superutilisateur pour accéder à l'interface admin par défaut de Django

### Données de Test

   On utilise Factory-boy et  faker pour peupler la BDD de test localement.

   ex: pour générer des questions avec des réponses par défaut,  dans le terminal lancer le module shell de Django faire la commande suivante :
   
      from faq.factory import ResolvedQuestionFactory
      ResolvedQuestionFactory.create_batch(42) 

   Ce sera pareil pour les autres classes

### Démarrage du serveur 
  - Aller dans le répertoire src
  - Lancer la commande : python3.11 manage.py runserver
  - Dans un autre terminal, dans la racine du projet lancer la commande :  npm run dev
  - Un Api est servi sur l'endpoint : {srv-url}/faq/api/v1/questions. on peut utiliser httpie pour tester la requête : 

    ex: pour avoir la liste des questions dèja résolues :   
    pip install httpie (si httpie n'est pas encore installé)
    HTTP -a {bob}:{mdpdebob} http://127.0.0.1:8000/faq/api/v1/questions 
    
    ex: pour passer des paramètres dans le endpoint
    HTTP -a bob:{mdpdebob} http://127.0.0.1:8000/faq/api/v1/questions\?usename\=Aina

## Déploiement
## Test
Les tests se trouve dans le dossier faq/tests/
Utiliser la commande : python manage.py test pour exécuter tout les tests disponibles dans le code

## CI/CD
