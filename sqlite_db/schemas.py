from typing import List, Optional

from pydantic import BaseModel


class LeituraBase(BaseModel):
    device: int
    leitura: float
    timestamp: int


class LeituraCreate(LeituraBase):
    pass


class Leitura(LeituraBase):
    id: int

    class Config:
        orm_mode = True
