FROM python:3.8.5
COPY ..
RUN sudo apt update
RUN apt install python3-pip
RUN apt install docker
RUN apt install nginx
RUN apt install gunicorn
RUN apt install postgresql postgresql-contrib
RUN pip install -r /code/requirements.txt
WORKDIR /code
CMD gunicorn yamdb_final.wsgi:application --bind 0.0.0.0:8000
