import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import backend.cruds.color as color_cruds
import backend.schema.color as color_schema
from backend.db import get_db
from backend.models.color import Color
from backend.services.sound_research import sound_research
from backend.utils.decode import get_payload_from_token
from backend.utils.download import download_blob
from backend.utils.makecolor import feature_to_color

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/color/getall", response_model=list[color_schema.ColorResponse])
async def get_all(db=Depends(get_db)):
    records = db.query(Color).all()
    return records


@router.get("/color/get", response_model=color_schema.ColorResponse)
async def matching(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    payload = get_payload_from_token(token)
    mail = payload.get("mail")
    hashed_password = payload.get("hashed_password")
    user_data = color_cruds.search_user(db, mail, hashed_password)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    color_data = db.query(Color).filter(Color.id == user_data.user_id).first()
    if color_data is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return color_schema.MatchingResponse(
        id=color_data.id, color1=color_data.color1, color2=color_data.color2
    )


@router.post("/color/record", response_model=color_schema.ColorResponse)
async def recording(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Assuming you have a database session and models set up
    payload = get_payload_from_token(token)
    mail = payload.get("mail")
    hashed_password = payload.get("hashed_password")
    user_data = color_cruds.search_user(db, mail, hashed_password)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    file_path = color_cruds.get_filepath_by_id(db, user_data.user_id)
    download_blob("yanbaru-eisa-storage-bucket-prod", file_path, "/tmp/hoge.ogg")
    if not os.path.exists("/tmp/hoge.ogg"):
        raise HTTPException(status_code=404, detail="File not found")
    feature = sound_research("/tmp/hoge.ogg")
    color1_data, color2_data = feature_to_color(feature)
    color_data = color_cruds.registar_color(
        db, user_data.user_id, color1_data, color2_data
    )
    os.remove("/tmp/hoge.ogg")
    return color_schema.ColorResponse(
        id=color_data.id, color1=color_data.color1, color2=color_data.color2
    )


@router.put("/color/update", response_model=color_schema.ColorResponse)
async def get_recording(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = get_payload_from_token(token)
    mail = payload.get("mail")
    hashed_password = payload.get("hashed_password")
    try:
        user_data = color_cruds.search_user(db, mail, hashed_password)
        if user_data is None:
            raise HTTPException(status_code=404, detail="User not found")
        record_id = user_data.user_id
        record = db.query(Color).filter(Color.id == record_id).first()
        if record is None:
            raise HTTPException(status_code=404, detail="Record not found")
        # Update the record as needed
        file_path = color_cruds.get_filepath_by_id(db, user_data.user_id)
        download_blob("yanbaru-eisa-storage-bucket-prod", file_path, "/tmp/hoge.ogg")
        if not os.path.exists("/tmp/hoge.ogg"):
            raise HTTPException(status_code=404, detail="File not found")
        feature = sound_research("/tmp/hoge.ogg")
        os.remove("/tmp/hoge.ogg")
        color1_data, color2_data = feature_to_color(feature)
        updated_record = color_cruds.update_color(
            db, record.id, color1_data, color2_data
        )

        return color_schema.ColorResponse(
            id=updated_record.id,
            color1=updated_record.color1,
            color2=updated_record.color2,
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=404, detail=str(e))
