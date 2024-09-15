from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    eisafile = Column(String, nullable=False)
    Record = relationship("Record", back_populates="users")


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True)
    color1 = Column(String, nullable=False)
    color2 = Column(String, nullable=False)

    users = relationship("User", back_populates="Record")
