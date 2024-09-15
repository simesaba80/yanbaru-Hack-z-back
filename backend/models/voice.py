from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True, index=True)
    color1 = Column(String, nullable=False)
    color2 = Column(String, nullable=False)
