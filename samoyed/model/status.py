from sqlalchemy import Column, DATETIME, ForeignKey, SMALLINT, String

from samoyed.model import Base


class Status(Base):
    user_email = Column(ForeignKey("user.email"), primary_key=True)
    is_paid = Column(SMALLINT, nullable=True)
    is_printed_application_arrived = Column(SMALLINT, nullable=True)
    is_passed_first_apply = Column(SMALLINT, nullable=True)
    is_passed_interview = Column(SMALLINT, nullable=True)
    is_final_submit = Column(SMALLINT, nullable=True)
    submitted_at = Column(DATETIME, nullable=True)
    exam_code = Column(String(6), nullable=True)