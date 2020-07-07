from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.helpers import get_db_location

engine = create_engine(get_db_location(), connect_args={"check_same_thread": False})
# check_same_thread only used for SQLite, https://fastapi.tiangolo.com/tutorial/sql-databases/
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

