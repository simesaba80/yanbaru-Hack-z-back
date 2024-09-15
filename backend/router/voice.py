from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import backend.schema.voice as voice_schema
from backend.db import get_db
from backend.models.voice import Record, User
from backend.utils.decode import get_payload_from_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/recording", response_model=voice_schema.RecordingResponse)
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

    new_recording = Record(
        id=user_data.id,
        color1="#000000",
        color2="#FFFFFF",
        # Add other fields as necessary
    )
    record_data = db.query(Record).filter(Record.id == user_data.id).first()
    if record_data is not None:
        raise HTTPException(status_code=404, detail="Record already exists")
    db.add(new_recording)
    db.commit()
    db.refresh(new_recording)
    print(payload.get("user_id"))
    return voice_schema.RecordingResponse(
        id=new_recording.id, color1="#000000", color2=new_recording.color2
    )


@router.put("/recordingupdate", response_model=voice_schema.RecordingResponse)
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
        record = db.query(Record).filter(Record.id == record_id).first()
        if record is None:
            raise HTTPException(status_code=404, detail="Record not found")
        # Update the record as needed
        record.color1 = "#FF0000"  # Example update
        db.commit()
        db.refresh(record)

        return voice_schema.RecordingResponse(
            id=record.id, color1=record.color1, color2=record.color2
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=404, detail=str(e))
