from sqlalchemy import Column, Integer, DATETIME, ForeignKey

from samoyed.model import Base


class GedApplication(Base):
    user_email = Column(ForeignKey("user.email"), primary_key=True)
    ged_average_score = Column(Integer, nullable=True)
    created_at = Column(DATETIME, nullable=False)
    modified_at = Column(DATETIME, nullable=False)
