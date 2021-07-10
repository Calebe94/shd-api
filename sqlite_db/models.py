from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float 
from sqlalchemy.orm import relationship

from .database import Base


class Leituras(Base):
    __tablename__ = "leituras"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    device = Column(Integer)
    leitura = Column(Float)
    timestamp = Column(Integer)

