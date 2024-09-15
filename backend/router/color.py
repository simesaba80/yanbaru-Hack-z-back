from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import backend.schema.color as color_schema
from backend.db import get_db
from backend.models.color import Color, User
from backend.utils.decode import get_payload_from_token
from backend.utils.download import download_blob

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/color/getall", response_model=list[color_schema.ColorResponse])
async def get_all(db=Depends(get_db)):
    records = db.query(Color).all()
    return records


@router.get("/color/get", response_model=color_schema.ColorResponse)
async def matching(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    payload = get_payload_from_token(token)
    email = payload.get("email")
    password = payload.get("password")
    user_data = (
        db.query(User)
        .filter(User.email == email)
        .filter(User.password == password)
        .first()
    )
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    color_data = db.query(Color).filter(Color.id == user_data.id).first()
    if color_data is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return color_schema.MatchingResponse(
        color1=color_data.color1, color2=color_data.color2
    )


@router.post("/color/record", response_model=color_schema.ColorResponse)
async def recording(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Assuming you have a database session and models set up
    payload = get_payload_from_token(token)
    user_data = (
        db.query(User)
        .filter(User.email == payload.get("email"))
        .filter(User.password == payload.get("password"))
        .first()
    )
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    download_blob(
        "yanbaru-eisa-storage-bucket-prod", user_data.eisafile, "/tmp/hoge.ogg"
    )
    new_recording = Color(
        id=user_data.id,
        color1="#000000",
        color2="#FFFFFF",
        # Add other fields as necessary
    )
    record_data = db.query(Color).filter(Color.id == user_data.id).first()
    if record_data is not None:
        raise HTTPException(status_code=404, detail="Record already exists")
    db.add(new_recording)
    db.commit()
    db.refresh(new_recording)
    print(payload.get("user_id"))
    return color_schema.ColorResponse(
        id=new_recording.id, color1="#000000", color2=new_recording.color2
    )


@router.put("/color/update", response_model=color_schema.ColorResponse)
async def get_recording(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = get_payload_from_token(token)
    email = payload.get("email")
    password = payload.get("password")
    try:
        user_data = (
            db.query(User)
            .filter(User.email == email)
            .filter(User.password == password)
            .first()
        )
        if user_data is None:
            raise HTTPException(status_code=404, detail="User not found")
        record_id = user_data.id
        record = db.query(Color).filter(Color.id == record_id).first()
        if record is None:
            raise HTTPException(status_code=404, detail="Record not found")
        # Update the record as needed
        record.color1 = "#FF0000"  # Example update
        db.commit()
        db.refresh(record)

        return color_schema.ColorResponse(
            id=record.id, color1=record.color1, color2=record.color2
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=404, detail=str(e))
