# Description
API for Youtube project.
Thanks to him, you can make various requests to the project.
All command descriptions will be on the site after the deployment of this project: http://84.201.177.209:8000/redoc/

# Run
1. There is no need to pre-install anything in this project. All installations occur automatically when sent to github 
2. While in the project directory, open console and run the following commands:
    1) sudo docker-compose exec web python manage.py makemigrations
    2) sudo docker-compose exec web python manage.py migrate
    3) sudo docker-compose exec web python manage.py loaddata fixtures.json
    4) exit
    
# How to run autotest
While in the project directory, open console and run command (but these tests run automatically with deploy on server):
    pytest
    flake8 --max-line-length=119 --exclude=tests,migrations,venv .    

# Predefined data
Administrator: 
* username: admin 
* password: admin


# What I used
* Python
* Django
* Bootstrap
* PostgreSQL
* Docker
* Gunicorn
* Nginx

# Author
github = https://github.com/nNDVG/
https://hub.docker.com/

(https://github.com/nNDVG/yamdb_final/workflows/yamdb_workflow/badge.svg)