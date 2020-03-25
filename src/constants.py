import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_LOCATION = os.getenv("DATABASE_LOCATION")
ZIP_DIRECTORY = os.getenv('ZIP_DIRECTORY')
IBM_API_KEY = os.getenv("IBM_API_KEY")
SAVE_FOLDER = "src/temp_data/"