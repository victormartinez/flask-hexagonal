PROJECT_NAME = flask_hexagonal
APPLICATION = flask_hexagonal.main:app

default: help

help:
	@echo "	Commands:"
	@echo "		Application:"
	@echo "			up - Start containers."
	@echo "			run - Run application in development mode."
	@echo "			down - Stop containers."
	@echo "		Database:"
	@echo "			db_upgrade - Apply database migrations."
	@echo "			db_generate_revision - Generate database migrations."
	@echo "		Environment:"
	@echo "			clean - Remove temp files."
	@echo "			format - Format code and check style."
	@echo "		Testing:"
	@echo "			unit-test - Run unit tests."

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
	mypy $(PROJECT_NAME) --config-file ./pyproject.toml

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

unit-test:
	pytest tests/unit/ -vv