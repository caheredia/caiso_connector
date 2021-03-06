from sqlalchemy import REAL, TEXT, TIMESTAMP, Column, Integer

from .database import Base


class Lmp(Base):
    __tablename__ = "lmp"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(TIMESTAMP)
    node = Column(TEXT)
    mw = Column(REAL)
