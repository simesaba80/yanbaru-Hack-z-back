from fastapi import FastAPI

from backend.router import match, voice

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!"}


app.include_router(voice.router)
app.include_router(match.router)
