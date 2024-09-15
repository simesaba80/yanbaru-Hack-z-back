from pydantic import BaseModel, Field


class MatchingResponse(BaseModel):
    color1: str = Field(..., example="#000000")
    color2: str = Field(..., example="#FFFFFF")
