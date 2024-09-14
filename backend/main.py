from fastapi import FastAPI

from backend.router import voice

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!"}


app.include_router(voice.router)
