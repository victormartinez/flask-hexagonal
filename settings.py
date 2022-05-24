from decouple import config


DB_USER = config("DB_USER", "")
DB_PASS = config("DB_PASS", "")
DB_HOST = config("DB_HOST", "")
DB_PORT = config("DB_PORT", default="5432")
DB_NAME = config("DB_NAME", "")


def build_database_uri() -> str:
    # As alembic.ini needs separated DB vars,
    # we can't return SQLALCHEMY_DATABASE_URI directly.
    # flask_hexagonal/infrastructure/alembic/env.py:28
    return f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
