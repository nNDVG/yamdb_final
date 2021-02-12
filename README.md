# Description
API for Youtube project.
Thanks to him, you can make various requests to the project.
All command descriptions will be on the site after the deployment of this project: http://130.193.43.113:8000/redoc/

# Run
1. There is no need to pre-install anything in this project. All installations occur automatically when sent to github.
2. If you want to migrate the database, you need to run the command:
    mirgations start

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