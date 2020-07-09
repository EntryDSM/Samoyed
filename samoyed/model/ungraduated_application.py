from sqlalchemy import Column, DATETIME, ForeignKey, Integer, String

from samoyed.model import Base


class UnGraduatedApplication(Base):
    user_email = Column(ForeignKey("user.receipt_code"), primary_key=True)
    student_number = Column(String(5), nullable=True)
    school_code = Column(ForeignKey("school.school_code"), nullable=True)
    school_tel = Column(String(20), nullable=True)
    volunteer_time = Column(Integer, nullable=True)
    full_cut_count = Column(Integer, nullable=True)
    period_cut_count = Column(Integer, nullable=True)
    late_count = Column(Integer, nullable=True)
    early_leave_count = Column(Integer, nullable=True)
    korean = Column(String(6), nullable=True)
    social = Column(String(6), nullable=True)
    history = Column(String(6), nullable=True)
    math = Column(String(6), nullable=True)
    science = Column(String(6), nullable=True)
    tech_and_home = Column(String(6), nullable=True)
    english = Column(String(6), nullable=True)
    created_at = Column(DATETIME, nullable=False)
    modified_at = Column(DATETIME, nullable=False)
