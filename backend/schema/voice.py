from pydantic import BaseModel, Field


class RecordingResponse(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="simesaba")


class RecordingRequest(BaseModel):
    name: str = Field(..., example="simesaba")
    email: str = Field(..., example="feynman@example.com")
    password: str = Field(..., example="password")
