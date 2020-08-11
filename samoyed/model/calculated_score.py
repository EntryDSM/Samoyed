from sqlalchemy import Column, DATETIME, ForeignKey, DECIMAL, Integer

from samoyed.model import Base


class CalculatedScore(Base):
    user_receipt_code = Column(ForeignKey("user.receipt_code"), primary_key=True)
    volunteer_score = Column(DECIMAL(10, 5), nullable=True)
    attendance_score = Column(Integer, nullable=True)
    conversion_score = Column(DECIMAL(10, 5), nullable=True)
    final_score = Column(DECIMAL(10, 5), nullable=True)
    first_grade_score = Column(DECIMAL(3, 3), nullable=True)
    second_grade_score = Column(DECIMAL(3, 3), nullable=True)
    third_grade_score = Column(DECIMAL(3, 3), nullable=True)
    created_at = Column(DATETIME, nullable=False)
    modified_at = Column(DATETIME, nullable=False)
