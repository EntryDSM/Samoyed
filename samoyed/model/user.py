from sqlalchemy import Column, DATETIME, Integer, String, Enum, SMALLINT, DATE

from samoyed.model import Base


class User(Base):
    email = Column(String(100), primary_key=True)
    password = Column(String(100), nullable=True)
    receipt_code = Column(Integer, autoincrement=True)
    apply_type = Column(Enum("COMMON", "MEISTER", "SOCIAL_ONE_PARENT",
                             "SOCIAL_FROM_NORTH", "SOCIAL_MULTICULTURAL",
                             "SOCIAL_BASIC_LIVING", "SOCIAL_LOWEST_INCOME",
                             "SOCIAL_TEEN_HOUSEHOLDER"), nullable=True)
    additional_type = Column(Enum("NATIONAL_MERIT", "PRIVILEGED_ADMISSION", "NOT_APPLICABLE"))
    grade_type = Column(Enum("GED", "UNGRADUATED", "GRADUATED"), nullable=True)
    is_daejeon = Column(SMALLINT, nullable=True)
    name = Column(String(15), nullable=True)
    sex = Column(Enum("FEMALE", "MALE"), nullable=True)
    birth_date = Column(DATE, nullable=True)
    parent_name = Column(String(15), nullable=True)
    parent_tel = Column(String(20), nullable=True)
    application_tel = Column(String(20), nullable=True)
    address = Column(String(250), nullable=True)
    detail_address = Column(String(250), nullable=True)
    post_code = Column(String(5), nullable=True)
    user_photo = Column(String(45), nullable=True)
    home_tel = Column(String(45), nullable=True)
    self_introduction = Column(String(1600), nullable=True)
    study_plan = Column(String(1600), nullable=True)
    created_at = Column(DATETIME, nullable=False)
    modified_at = Column(DATETIME, nullable=False)
