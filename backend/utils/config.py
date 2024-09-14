import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

# Load environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
