from sqlalchemy import Column, Integer, DATETIME, ForeignKey, DATE

from samoyed.model import Base


class GedApplication(Base):
    __tablename__ = 'ged_application'

    user_receipt_code = Column(ForeignKey("user.receipt_code"), primary_key=True)
    ged_average_score = Column(Integer, nullable=True)
    ged_pass_date = Column(DATE, nullable=True)
    created_at = Column(DATETIME, nullable=False)
    modified_at = Column(DATETIME, nullable=False)
