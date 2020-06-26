from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from samoyed import DATABASE_URL

engine = create_engine(DATABASE_URL, encoding="utf-8")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
