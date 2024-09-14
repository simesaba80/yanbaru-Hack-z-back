from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

import backend.schema.match as match_schema
from backend.utils import config

router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=401, detail="Invalid authentication credentials"
            )
        return user_id
    except JWTError:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )


@router.get("/matching", response_model=match_schema.MatchingResponse)
async def matching(user_id: str = Depends(get_current_user)):
    # Implement your logic here to return different responses based on the user_id
    pass
