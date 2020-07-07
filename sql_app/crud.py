from sqlalchemy.orm import Session

from . import models


def get_lmps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lmp.node).distinct().offset(skip).limit(limit).all()
