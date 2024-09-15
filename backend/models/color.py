from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    mail = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    Color = relationship("Color", back_populates="users")
    Eisafile = relationship("Eisafile", back_populates="users")


class Eisafile(Base):
    __tablename__ = "eisafiles"

    id = Column(String, ForeignKey("users.user_id"), primary_key=True, index=True)
    file_path = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)

    users = relationship("User", back_populates="Eisafile")


class Color(Base):
    __tablename__ = "colors"

    id = Column(String, ForeignKey("users.user_id"), primary_key=True, index=True)
    color1 = Column(String, nullable=False)
    color2 = Column(String, nullable=False)

    users = relationship("User", back_populates="Color")
