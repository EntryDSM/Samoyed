from sqlalchemy import Column, DATETIME, ForeignKey, SMALLINT

from samoyed.model import Base


class Status(Base):
    user_email = Column(ForeignKey("user.email"))
    is_paid = Column(SMALLINT)
    is_printed_application_arrived = Column(SMALLINT)
    is_passed_first_apply = Column(SMALLINT)
    is_passed_interview = Column(SMALLINT)
    is_final_submit = Column(SMALLINT)
    submitted_at = Column(DATETIME)
    exam_code = Column(DATETIME)
