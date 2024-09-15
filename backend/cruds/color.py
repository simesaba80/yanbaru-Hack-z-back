from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.models.color import Color, Eisafile, User


def search_user(db: Session, mail: str, hashed_password: str):
    return (
        db.query(User)
        .filter(User.mail == mail)
        .filter(User.hashed_password == hashed_password)
        .first()
    )


def registar_color(db: Session, id: str, color1: str, color2: str):
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


def update_color(db: Session, id: str, color1: str, color2: str):
    record = db.query(Color).filter(Color.id == id).first()
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    record.color1 = color1
    record.color2 = color2
    db.commit()
    db.refresh(record)
    return record


def get_filepath_by_id(db: Session, id: str):
    eisa_file = db.query(Eisafile).filter(Eisafile.id == id).first()
    if eisa_file is None:
        raise HTTPException(status_code=404, detail="User not found")
    return eisa_file.file_path
