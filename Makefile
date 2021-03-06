PROJECT_NAME = flask_hexagonal
APPLICATION = flask_hexagonal.main:app

default: help

help:
	@echo "All Commands:"
	@echo "		clean - Remove temp files."
	@echo "		down - Stop containers."
	@echo "		db_upgrade - Apply database migrations."
	@echo "		db_generate_revision - Generate database migrations."
	@echo "		format - Format code and check style."
	@echo "		up - Start containers."
	@echo "		run - Run application in development mode."

clean:
	- @find . -name "*.pyc" -exec rm -rf {} \;
	- @find . -name "__pycache__" -delete
	- @find . -name "*.pytest_cache" -exec rm -rf {} \;
	- @find . -name "*.mypy_cache" -exec rm -rf {} \;

format:
	######## FORMATS THE CODE AUTOMATICALLY ########
	black -l 88 -t py310 --skip-string-normalization $(PROJECT_NAME) $(TEST_FOLDER)
	unify --in-place --recursive --quote '"' $(PROJECT_NAME) $(TEST_FOLDER)
	isort --skip-glob "migrations/**" --profile black .

	######## CHECK IF SOMETHING STILL NEEDS FORMATTING ########
	black -l 88 -t py310 --skip-string-normalization --check $(PROJECT_NAME) $(TEST_FOLDER)

	######## CHECK TYPING ########
	mypy --python-version 3.10 --ignore-missing-imports --disallow-untyped-defs --disallow-untyped-calls $(PROJECT_NAME)/

	# code style
	flake8 $(PROJECT_NAME) $(TEST_FOLDER)

	# ensure double quote
	unify --check-only --recursive --quote '"' $(PROJECT_NAME) $(TEST_FOLDER)

	isort --profile black --skip-glob "migrations/**" -c .

	# check security issues
	bandit -r $(PROJECT_NAME)

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

