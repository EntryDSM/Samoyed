from sqlalchemy import Column, DATETIME, ForeignKey, DECIMAL, Integer

from samoyed.model import Base


class CalculatedScore(Base):
    user_email = Column(ForeignKey("user.email"), primary_key=True)
    volunteer_score = Column(DECIMAL(10, 5))
    attendance_score = Column(Integer)
    conversion_score = Column(DECIMAL(10, 5))
    final_score = Column(DECIMAL(10, 5))
    created_at = Column(DATETIME, nullable=True)
    modified_at = Column(DATETIME, nullable=True)
