# Description
API for Youtube project.
Thanks to him, you can make various requests to the project.
All command descriptions will be on the site after the deployment of this project: http://domen/redoc/
# Run
## To install on a local computer, you must:
* Install Docker and Docker-Compose (only for linux)
* Download project files from the repository or clone it: https://github.com/nNDVG/yamdb_final.git
#### Enter the following command:
    docker exec -it api_yamdb_web_1 bash
    apt update
    apt install nano
#### You need to create an .env file in which to specify environment variables (for example): 
  - DB_NAME = postgres
  - DB_USER = postgres
  - DB_PASSWORD = postgres
  - DB_HOST = db
  - DB_PORT = 5432

#### To do this, enter the following command and enter the appropriate data (the ones above):
    nano .env 

#### In the <project_name>/foodgram/ project directory, enter the command:
    docker-compose up -d

#### To create a superuser system, run the command:
     docker-compose exec foodgram_web_1 python manage.py creates superuser

# How to run autotest
### While in the project directory, open console and run command (but these tests run automatically with deploy on server):
- pytest
- flake8 --max-line-length=119 --exclude=tests,migrations,venv .    

# Author
 - https://github.com/nNDVG/
 - https://hub.docker.com/u/ndvg/

# Tech stack:
* Python
* Django
* Django REST
* PostgreSQL
* Gunicorn
* Nginx
* Docker
* GitHub actions
