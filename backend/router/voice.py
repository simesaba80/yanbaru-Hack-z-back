from fastapi import APIRouter

import backend.schema.voice as voice_schema

router = APIRouter()


@router.post("/recording", response_model=voice_schema.RecordingResponse)
async def recording(recording_body: voice_schema.RecordingRequest):
    pass
