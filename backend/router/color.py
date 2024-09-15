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
    user_data = color_cruds.search_user(db, email, password)
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
    email = payload.get("email")
    password = payload.get("password")
    user_data = color_cruds.search_user(db, email, password)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    download_blob(
        "yanbaru-eisa-storage-bucket-prod", user_data.eisafile, "/tmp/hoge.ogg"
    )
    feature = sound_research("/tmp/hoge.ogg")
    color1_data = (
        "#"
        + format(feature.speech_rate * 16, "x")
        + format(feature.pitch * 16, "x")
        + format(feature.syllable_1 * 16, "x")
    )
    color2_data = (
        "#"
        + format(feature.syllable_2 * 16, "x")
        + format(feature.syllable_3 * 16, "x")
        + format(feature.syllable_4 * 16, "x")
    )
    color_data = color_cruds.registar_color(db, user_data.id, color1_data, color2_data)
    print(payload.get("user_id"))
    return color_schema.ColorResponse(
        id=color_data.id, color1=color_data.color1, color2=color_data.color2
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
        user_data = color_cruds.search_user(db, email, password)
        if user_data is None:
            raise HTTPException(status_code=404, detail="User not found")
        record_id = user_data.id
        record = db.query(Color).filter(Color.id == record_id).first()
        if record is None:
            raise HTTPException(status_code=404, detail="Record not found")
        # Update the record as needed
        record.color1 = "#FF0000"  # Example update
        updated_record = color_cruds.update_color(
            db, record.id, record.color1, record.color2
        )

        return color_schema.ColorResponse(
            id=updated_record.id,
            color1=updated_record.color1,
            color2=updated_record.color2,
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=404, detail=str(e))
