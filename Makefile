compose-build:
	docker compose build

compose-up:
	docker compose build -d

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver

env:
	source env/bin/activate