from pydantic import BaseModel, Field


class RecordingResponse(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="simesaba")
    filepath: str = Field(..., example="https://file/to/path")


class RecordingRequest(BaseModel):
    name: str = Field(..., example="simesaba")
    filepath: str = Field(..., example="https://file/to/path")
