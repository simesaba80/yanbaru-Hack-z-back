from fastapi import APIRouter

import backend.schema.voice as voice_schema

router = APIRouter()


@router.post("/recording", response_model=voice_schema.RecordingResponse)
async def recording(recording_body: voice_schema.RecordingRequest):
    pass


@router.get("/recording/{recording_id}", response_model=voice_schema.RecordingResponse)
async def get_recording(recording_body: voice_schema.RecordingRequest):
    pass
