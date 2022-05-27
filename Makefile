PROJECT_NAME = flask_hexagonal
APPLICATION = flask_hexagonal.main:app

default: help

help:
	@echo "All Commands:"
	@echo "	Env:"
	@echo "		run - Run application in development mode."
	@echo "		clean - Remove temp files."
	@echo "		down - Stop containers."
	@echo "		db_upgrade - Apply database migrations."
	@echo "		db_generate_revision - Generate database migrations."
	@echo "		up - Start containers."

clean:
	- @find . -name "*.pyc" -exec rm -rf {} \;
	- @find . -name "__pycache__" -delete
	- @find . -name "*.pytest_cache" -exec rm -rf {} \;
	- @find . -name "*.mypy_cache" -exec rm -rf {} \;

db_upgrade:
	alembic upgrade head

db_generate_revision:
	alembic revision --autogenerate

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

run: up db_upgrade
	gunicorn $(APPLICATION) --workers 4 --bind 0.0.0.0:5000

