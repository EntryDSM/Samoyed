from sqlalchemy import Column, String

from model import Base


class Admin(Base):
    email = Column(String(100), primary_key=True)
    password = Column(String(100), nullable=False)
    name = Column(String(45), nullable=False)
