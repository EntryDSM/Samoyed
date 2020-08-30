from sqlalchemy import Column, String

from samoyed.model import Base


class School(Base):
    __tablename__ = 'school'

    school_code = Column(String(10), primary_key=True)
    school_name = Column(String(45), nullable=True)
    school_full_name = Column(String(45), nullable=False)
    school_address = Column(String(100), nullable=False)
