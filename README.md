# P11_Gudlft

## Présentation

Ce programme est une version beta d'une application qui aide à la gestion et à l'organisation des compétitions de force (deadlifting, strongman) en Amérique du Nord et en Australie. L'objectif est d'obtenir un programme simple et peu couteux qui permet à chaque club de : 

 * se connecter avec leur adresse email
 * visualuser les points des autres clubs
 * connaitre les places disponibles sur une compétition
 * réserver des places d'une compétition
 * mettre à jour automatiquement le décompte de points

## Pour commencer

Les instructions ci dessous vous aiderons à exécuter correctement ce programme.

## Pré-requis

* Python 3 installé [Télécharger Python](https://www.python.org/downloads/)
* Savoir naviguer dans les dossiers & fichiers à partir d'un terminal.

## Installation

Pour un bon fonctionnement, il est préférable d'exécuter le programme dans un environnement virtuel. Pour cela, ci dessous les étapes à suivre:

1. **Téléchargement du projet.**

    1. Depuis votre terminal, placez vous à l'endroit souhaité:
    
    ```cd [chemin d'accès]```  
    
    2. Creer un nouveau dossier:
    
    ```mkdir [nom de votre dossier]```
    
    3. Copier le programme source:
    
    ```git clone https://github.com/JM-Duval/P11_Gudlft.git```
    

Vous devez voir (depuis votre explorateur) les dossiers suivants: 

 * project/
 * templates/
 * tests/

Et les fichiers suivants:

 * .DS_Store
 * .coverage
 * .coveragerc
 * .gitignore
 * clubs.json
 * competitions.json
 * manage.py
 * requirements.txt
 * server.py

2. **Creer un environnement virtuel.**

Depuis windows/mac/linux: ```python3 -m venv env```

3. **Activer l'environnement.**

Depuis windows: ```env\Scripts\activate.bat```

Depuis mac/linux: ```source env/bin/activate```

Si vous rencontrez des difficultés ou si vous souhaitez plus de détails sur l'installation d'un environnement virtuel, vous pouvez vous reporter à la documentation Python:
[Documentation Python](https://www.python.org/doc/)

4. **Installer les paquets.**

```pip install -r requirements.txt```

En executant la commande: pip freeze, vous devez voir apparaitre cette liste: 
- asgiref==3.4.1
- async-generator==1.10
- atomicwrites==1.4.0
- attrs==21.2.0
- beautifulsoup4==4.10.0
- Brotli==1.0.9
- certifi==2021.10.8
- cffi==1.15.0
- charset-normalizer==2.0.7
- click==7.1.2
- colorama==0.4.4
- ConfigArgParse==1.5.3
- coverage==6.1.2
- cryptography==35.0.0
- Django==3.2.9
- Flask==2.0.2
- Flask-BasicAuth==0.2.0
- Flask-Cors==3.0.10
- Flask-Testing==0.8.1
- gevent==21.8.0
- geventhttpclient==1.5.3
- greenlet==1.1.2
- h11==0.12.0
- idna==3.3
- iniconfig==1.1.1
- itsdangerous==2.0.1
- Jinja2==3.0.3
- locust==2.5.0
- MarkupSafe==2.0.1
- msgpack==1.0.2
- outcome==1.1.0
- packaging==21.2
- pluggy==1.0.0
- psutil==5.8.0
- py==1.11.0
- pycparser==2.21
- pyOpenSSL==21.0.0
- pyparsing==2.4.7
- pytest==6.2.5
- pytest-cov==3.0.0
- pytest-django==4.4.0
- pytest-flask==1.2.0
- pytest-mock==3.6.1
- pytz==2021.3
- pywin32==302
- pyzmq==22.3.0
- requests==2.26.0
- roundrobin==0.0.2
- selenium==4.0.0
- six==1.16.0
- sniffio==1.2.0
- sortedcontainers==2.4.0
- soupsieve==2.3.1
- sqlparse==0.4.2
- toml==0.10.2
- tomli==1.2.2
- trio==0.19.0
- trio-websocket==0.9.2
- typing_extensions==4.0.0
- urllib3==1.26.7
- Werkzeug==2.0.2
- wsproto==1.0.0
- zope.event==4.5.0
- zope.interface==5.4.0 

5. **Lancement du programme.**

Avant de lancer Flask, vous devez le configurez en tapant la commande suivante (a l'endroit ou se situe votre dossier):

```export FLASK_APP=server```

Puis exécuter la commande suivante:

```flask run```

Losque Flask est en fonctionnement, le message suivant doit apparaitre sur votre terminal:

```
Serving Flask app 'server' (lazy loading)
Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
Debug mode: off
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [23/Nov/2021 08:16:30] "GET / HTTP/1.1" 200 -
```

Copiez l'adresse ```http://127.0.0.1:5000/``` dans la barre de votre navigateur web. Vous devez accèder directement sur le site internet concerné.


## Fabriqué avec
[PyCharm Community Edition 2020.2.3 x64](https://pycharm-community-edition.fr.softonic.com/) - Editeur de textes


## Auteurs

* **JM Duval** 

