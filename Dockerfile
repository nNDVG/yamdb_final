FROM python:3.8.5
COPY . .
RUN pip install -r /code/requirements.txt
WORKDIR /code
CMD gunicorn yamdb_final.wsgi:application --bind 0.0.0.0:8000
