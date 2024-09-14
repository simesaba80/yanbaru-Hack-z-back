import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")


config = Config()
