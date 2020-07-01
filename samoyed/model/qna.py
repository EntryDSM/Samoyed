from sqlalchemy import Column, String, DATETIME, ForeignKey, Integer, Enum, SMALLINT

from samoyed.model import Base


class Qna(Base):
    qna_id = Column(Integer)
    admin_email = Column(ForeignKey("admin.email"))
    user_email = Column(ForeignKey("user.email"))
    to = Column(Enum("admin, student"), nullable=True)
    content = Column(String(100), nullable=True)
    created_time = Column(DATETIME, nullable=True)
    is_read = Column(SMALLINT, nullable=True)
