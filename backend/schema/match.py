from pydantic import BaseModel, Field


class MatchingResponse(BaseModel):
    name: str = Field(..., example="simesaba")
