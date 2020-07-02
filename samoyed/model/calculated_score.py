from sqlalchemy import Column, DATETIME, ForeignKey, DECIMAL, Integer

from samoyed.model import Base


class CalculatedScore(Base):
    user_email = Column(ForeignKey("user.email"), primary_key=True)
    volunteer_score = Column(DECIMAL(10, 5), nullable=True)
    attendance_score = Column(Integer, nullable=True)
    conversion_score = Column(DECIMAL(10, 5), nullable=True)
    final_score = Column(DECIMAL(10, 5), nullable=True)
    created_at = Column(DATETIME, nullable=False)
    modified_at = Column(DATETIME, nullable=False)
