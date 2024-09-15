from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.models.color import Color, User


def search_user(db: Session, email: str, password: str):
    return (
        db.query(User)
        .filter(User.email == email)
        .filter(User.password == password)
        .first()
    )


def registar_color(db: Session, id: int, color1: str, color2: str):
    new_color = Color(
        id=id,
        color1=color1,
        color2=color2,
        # Add other fields as necessary
    )
    record_data = db.query(Color).filter(Color.id == new_color.id).first()
    if record_data is not None:
        raise HTTPException(status_code=404, detail="Record already exists")
    db.add(new_color)
    db.commit()
    db.refresh(new_color)
    return new_color


def update_color(db: Session, id: int, color1: str, color2: str):
    record = db.query(Color).filter(Color.id == id).first()
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    record.color1 = color1
    record.color2 = color2
    db.commit()
    db.refresh(record)
    return record
