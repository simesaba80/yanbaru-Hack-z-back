from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

import backend.schema.match as match_schema
from backend.db import get_db
from backend.models.voice import Record, User
from backend.utils.decode import get_payload_from_token

router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/matching", response_model=match_schema.MatchingResponse)
async def matching(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    payload = get_payload_from_token(token)
    email = payload.get("email")
    password = payload.get("password")
    user_data = (
        db.query(User)
        .filter(User.email == email)
        .filter(User.password == password)
        .first()
    )
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    color_data = db.query(Record).filter(Record.id == user_data.id).first()
    if color_data is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return match_schema.MatchingResponse(
        color1=color_data.color1, color2=color_data.color2
    )
    # Implement your logic here to return different responses based on the user_id
    pass
