from sqlalchemy import Column, String

from model import Base


class School(Base):
    school_code = Column(String(10), primary_key=True)
    school_name = Column(String(45), nullable=True)
    school_full_name = Column(String(45), nullable=False)
    school_address = Column(String(100), nullable=False)
