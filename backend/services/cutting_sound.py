from fastapi import HTTPException
from pydub.silence import split_on_silence


def cutting_sound(sound):
    chunks = split_on_silence(
        sound, min_silence_len=10, silence_thresh=-35, keep_silence=100
    )

    cutted_sound = sum(chunks)

    if cutted_sound < 1000:
        raise HTTPException(status_code=400, detail="Bad Request")

    return cutted_sound
