from fastapi import HTTPException


def speech_rating(sound):
    # 音声の長さ（ミリ秒）
    duration_ms = len(sound)

    thresholds = [
        1000,
        1179,
        1357,
        1536,
        1714,
        1893,
        2071,
        2250,
        2429,
        2607,
        2786,
        2964,
        3143,
        3321,
        3500,
    ]

    if duration_ms > 3500:
        return 15

    # 話速の分類
    for i, threshold in enumerate(thresholds):
        if duration_ms <= threshold:
            return i

    raise HTTPException(status_code=400, detail="Bad Request")
