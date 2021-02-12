db-down: ## Down Docker Postgres container for migrations
    sudo docker-compose stop

migrate: ## Make and run migrations
    sudo docker-compose exec web python manage.py makemigrations
    sudo docker-compose exec web python manage.py migrate

db-up: ## Pull and start the Docker Postgres container in the background
    sudo docker pull postgres
    sudo docker-compose up -d

