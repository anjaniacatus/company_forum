[![fr](https://img.shields.io/badge/lang-fr-red.svg)](https://github.com/anjaniacatus/company_forum/blob/main/README.fr.md)
[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/anjaniacatus/company_forum/blob/main/README.md)

## Frequently asked questions

This is an application proposal to allow a company to  manage and reply questions  from there customers 

## Specifications

- lambda visitors can view and search for replied questions
- A company user can look and search for questions and replied to them
- An authenticated user can ask new questions and follow up on them
- An api is needed at least to retrieve all of the questions depending on his states (resolved, pending, ....) 
- We have to use Django and DRF for the implementation


## Setting up the project locally

## Installation
- git clone https://github.com/anjaniacatus/company_forum
- cd company_forum

### Frontend
- In the project root launch  : npm install

### Backend
 - in the root project , create a 'virtual env' :  python3 -m venv venv
 - Activate it : source venv/bin/activate
 - Install dependencies though  src/requirements.txt :   pip install -r src/requirements.txt

### Databases
 - This app use PostgresSQL
 - Before lunching migrations, Create a local database using the name configured in settings.py
 - Migration : go to the src/QuestionBox/ then execute the  command : python manage.py migrate
 - You have to create a superuser for the django admin

### Test

   we use  Factory-boy and  faker for seeding data

   ex: from  the Django Shell, execute the following command  to generate some  questions randomly :
   
      from faq.factory import ResolvedQuestionFactory
      ResolvedQuestionFactory.create_batch(42) 

   You can use the same process for the other classes

### Launch the server locally
  - in the src directory execute : python3.11 manage.py runserver
  - In the other terminal, inside the root project du projet execute :  npm run dev
  - the api is served on this endpoint : {srv-url}/faq/api/v1/questions   

    eg: for testing the endpoint  
    pip install httpie (if you want to use it , but curl also can work)
    HTTP -a {bob}:{mdpdebob} http://127.0.0.1:8000/faq/api/v1/questions 
    
    eg: testing the endpoint with some filter
    HTTP -a bob:{mdpdebob} http://127.0.0.1:8000/faq/api/v1/questions\?usename\=Aina

## Deployment
## Test
tests are inside the faq/tests/ directory
how to lunch the test locally  : python manage.py test 

## CI/CD
