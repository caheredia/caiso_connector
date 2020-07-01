from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.helpers import DATABASE_LOCATION

SQLALCHEMY_DATABASE_URL = "sqlite:///src/lmp.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# check_same_thread only used for SQLite, https://fastapi.tiangolo.com/tutorial/sql-databases/
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
