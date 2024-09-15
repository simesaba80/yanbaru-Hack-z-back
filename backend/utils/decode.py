import base64
import json

from fastapi import HTTPException, status


# Base64デコード用の関数
def base64_decode(data: str):
    # Base64 URLセーフデコードを行う
    padding_needed = 4 - (len(data) % 4)
    data += "=" * padding_needed  # パディングを追加
    return base64.urlsafe_b64decode(data)


# JWTトークンからペイロード部分をデコードしてJSONにする関数
def get_payload_from_token(token: str):
    try:
        # トークンをドットで分割し、ペイロード部分を取り出す
        payload_base64 = token.split(".")[1]
        decoded_payload = base64_decode(payload_base64)
        payload_json = json.loads(decoded_payload)
        return payload_json
    except (IndexError, json.JSONDecodeError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token format",
        )
