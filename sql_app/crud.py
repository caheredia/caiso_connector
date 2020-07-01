from sqlalchemy.orm import Session

from . import models, schemas


def get_lmps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lmp).offset(skip).limit(limit).all()


def bulk_create_lmp(db: Session, csv_file: str):
    """Take a csv file as input and bulk loads rows."""
    db_lmp = models.Lmp()
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
