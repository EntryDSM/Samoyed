from sqlalchemy import Column, String, DATETIME, ForeignKey, Integer, Enum, SMALLINT

from samoyed.model import Base


class Qna(Base):
    qna_id = Column(Integer, primary_key=True)
    admin_email = Column(ForeignKey("admin.email"), nullable=True)
    user_email = Column(ForeignKey("user.receipt_code"), nullable=True)
    to = Column(String(20), nullable=False)
    content = Column(String(100), nullable=False)
    created_time = Column(DATETIME, nullable=False)
    is_read = Column(SMALLINT, nullable=False)
