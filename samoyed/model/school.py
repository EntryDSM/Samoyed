from sqlalchemy import Column, String

from samoyed.model import Base


class School(Base):
    school_code = Column(String(10))
    school_name = Column(String(45))
    school_full_name = Column(String(45), nullable=True)
    school_address = Column(String(100), nullable=True)
