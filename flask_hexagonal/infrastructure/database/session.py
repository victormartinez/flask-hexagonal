from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings

engine = create_engine(settings.build_database_uri())
Session = sessionmaker(engine)
