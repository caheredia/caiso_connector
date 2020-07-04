from datetime import datetime

from pydantic import BaseModel


class LmpBase(BaseModel):
    time: datetime
    node: str
    mw: float


class LmpCreate(LmpBase):
    pass


class Lmp(LmpBase):
    id: int

    class Config:
        orm_mode = True
