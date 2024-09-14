import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    DB_URL = os.getenv("DB_URL")


config = Config()
