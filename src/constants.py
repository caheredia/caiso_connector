import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_LOCATION = os.getenv("src/lmp.db")
ZIP_DIRECTORY = os.getenv('src/temp_data')
