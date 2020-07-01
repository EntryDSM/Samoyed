from sqlalchemy import Column, String, DATETIME, ForeignKey, Integer

from samoyed.model import Base


class GraduatedApplication(Base):
    user_email = Column(ForeignKey("user.email"), primary_key=True)
    student_number = Column(String(5))
    school_code = Column(ForeignKey("school.school_code"))
    school_tel = Column(String(20))
    volunteer_time = Column(Integer)
    full_cut_count = Column(Integer)
    period_cut_count = Column(Integer)
    late_count = Column(Integer)
    early_leave_count = Column(Integer)
    korean = Column(String(6))
    social = Column(String(6))
    history = Column(String(6))
    math = Column(String(6))
    science = Column(String(6))
    tech_and_home = Column(String(6))
    english = Column(String(6))
    created_at = Column(DATETIME, nullable=True)
    modified_at = Column(DATETIME, nullable=True)
