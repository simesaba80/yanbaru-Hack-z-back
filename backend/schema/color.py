from pydantic import BaseModel, Field


class ColorResponse(BaseModel):
    id: int = Field(..., example=1)
    color1: str = Field(..., example="#000000")
    color2: str = Field(..., example="#FFFFFF")
