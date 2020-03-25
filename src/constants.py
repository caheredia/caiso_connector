import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_LOCATION = "src/lmp.db"
ZIP_DIRECTORY = 'src/temp_data'
SAVE_FOLDER = "src/temp_data/"

# environment variables
IBM_API_KEY = os.getenv("IBM_API_KEY")
