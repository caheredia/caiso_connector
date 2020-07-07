from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models


def get_lmps(db: Session, skip: int = 0, limit: int = 100) -> list:
    return db.query(models.Lmp.node).distinct().offset(skip).limit(limit).all()


def get_row_count(db: Session) -> int:
    """
    Return number of rows in table
    """
    return db.query(func.max(models.Lmp.id)).first()[0]
