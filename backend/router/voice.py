import base64
import json

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import backend.schema.voice as voice_schema
from backend.db import get_db
from backend.models.voice import Record, User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Base64デコード用の関数
def base64_decode(data: str):
    # Base64 URLセーフデコードを行う
    padding_needed = 4 - (len(data) % 4)
    data += "=" * padding_needed  # パディングを追加
    return base64.urlsafe_b64decode(data)


# JWTトークンからペイロード部分をデコードしてJSONにする関数
def get_payload_from_token(token: str):
    try:
        # トークンをドットで分割し、ペイロード部分を取り出す
        payload_base64 = token.split(".")[1]
        decoded_payload = base64_decode(payload_base64)
        payload_json = json.loads(decoded_payload)
        return payload_json
    except (IndexError, json.JSONDecodeError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token format",
        )


@router.post("/recording", response_model=voice_schema.RecordingResponse)
async def recording(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Assuming you have a database session and models set up
    payload = get_payload_from_token(token)

    new_recording = Record(
        color1="#000000",
        color2="#FFFFFF",
        # Add other fields as necessary
    )
    db.add(new_recording)
    db.commit()
    db.refresh(new_recording)
    print(payload.get("user_id"))
    return voice_schema.RecordingResponse(
        id=new_recording.id, color1="#000000", color2=new_recording.color2
    )


@router.put("/recording/{recording_id}", response_model=voice_schema.RecordingResponse)
async def get_recording(
    token: str = Depends(oauth2_scheme),
    recording_id: int = None,
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
            raise HTTPException(status_code=404, detail="Recording not found")
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
