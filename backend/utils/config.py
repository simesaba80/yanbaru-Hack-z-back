import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    DB_URL = os.getenv("DB_URL")
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    BUCKET_NAME = os.getenv("BUCKET_NAME")


config = Config()
