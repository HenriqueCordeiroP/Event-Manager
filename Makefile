compose-build:
	docker compose build

compose-up:
	docker compose up -d

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver
