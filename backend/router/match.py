from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

import backend.schema.match as match_schema

router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
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
