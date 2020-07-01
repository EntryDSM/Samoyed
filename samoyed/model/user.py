from sqlalchemy import Column, DATETIME, Integer, String, Enum, SMALLINT, DATE

from samoyed.model import Base


class User(Base):
    email = Column(String(100))
    password = Column(String(100), nullable=True)
    receipt_code = Column(Integer, nullable=True)
    apply_type = Column(Enum("COMMON", "MEISTER", "SOCIAL_ONE_PARENT",
                             "SOCIAL_FROM_NORTH", "SOCIAL_MULTICULTURAL",
                             "SOCIAL_BASIC_LIVING", "SOCIAL_LOWEST_INCOME",
                             "SOCIAL_TEEN_HOUSEHOLDER"))
    additional_type = Column(Enum("NATIONAL_MERIT", "PRIVILEGED_ADMISSION", "NOT_APPLICABLE"))
    grade_type = Column(Enum("GED", "UNGRADUATED", "GRADUATED"))
    is_daejeon = Column(SMALLINT)
    name = Column(String(15))
    sex = Column(Enum("FEMALE", "MALE"))
    birth_date = Column(DATE)
    parent_name = Column(String(15))
    parent_tel = Column(String(20))
    application_tel = Column(String(20))
    address = Column(String(250))
    detail_address = Column(String(250))
    post_code = Column(String(5))
    user_photo = Column(String(45))
    home_tel = Column(String(45))
    self_introduction = Column(String(1600))
    study_plan = Column(String(1600))
    created_at = Column(DATETIME)
    modified_at = Column(DATETIME)

