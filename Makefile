PROJECT_NAME = flask_hexagonal
APPLICATION = flask_hexagonal.main:app

default: help

help:
	@echo "All Commands:"
	@echo "	Env:"
	@echo "		run - Run application in development mode."


run:
	gunicorn $(APPLICATION) --workers 4 --bind 0.0.0.0:5000
