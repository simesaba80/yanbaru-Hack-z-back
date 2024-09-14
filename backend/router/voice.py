from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import backend.schema.voice as voice_schema
from backend.db import get_db
from backend.models.voice import RecordingResponseModel

router = APIRouter()


@router.post("/recording", response_model=voice_schema.RecordingResponse)
async def recording(recording_body: voice_schema.RecordingRequest):
    # Assuming you have a database session and models set up

    db: Session = Depends(get_db)

    new_recording = RecordingResponseModel(
        color1=recording_body.color1,
        color2=recording_body.filepath,
        # Add other fields as necessary
    )
    db.add(new_recording)
    db.commit()
    db.refresh(new_recording)

    return voice_schema.RecordingResponse(
        id=new_recording.id, color1="#000000", color2=new_recording.filepath
    )


@router.put("/recording/{recording_id}", response_model=voice_schema.RecordingResponse)
async def get_recording(recording_body: voice_schema.RecordingRequest):
    pass
