from sqlalchemy import Column, DATETIME, Integer, String, Enum, SMALLINT, DATE

from samoyed.model import Base


class User(Base):
    receipt_code = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    apply_type = Column(String(20), nullable=True)
    additional_type = Column(String(20), nullable=True)
    grade_type = Column(String(20), nullable=True)
    is_daejeon = Column(SMALLINT, nullable=True)
    name = Column(String(15), nullable=True)
    sex = Column(String(20), nullable=True)
    birth_date = Column(DATE, nullable=True)
    parent_name = Column(String(15), nullable=True)
    parent_tel = Column(String(20), nullable=True)
    application_tel = Column(String(20), nullable=True)
    address = Column(String(250), nullable=True)
    detail_address = Column(String(250), nullable=True)
    post_code = Column(String(5), nullable=True)
    user_photo = Column(String(45), nullable=True)
    self_introduction = Column(String(1600), nullable=True)
    study_plan = Column(String(1600), nullable=True)
    created_at = Column(DATETIME, nullable=False)
    modified_at = Column(DATETIME, nullable=False)
