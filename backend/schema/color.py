from pydantic import BaseModel, Field


class ColorResponse(BaseModel):
    id: str = Field(..., example="testuser")
    color1: str = Field(..., example="#000000")
    color2: str = Field(..., example="#FFFFFF")
