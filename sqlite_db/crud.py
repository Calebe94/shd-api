from sqlalchemy.orm import Session
from . import models, schemas


def get_leitura(db: Session, device: int):
    return db.query(models.Leituras).filter(models.Leituras.device == device).order_by(models.Leituras.id.desc()).first()

def get_leitura_by_device(db: Session, device: int):
    return db.query(models.Leituras).filter(models.Leituras.device == device).first()

def create_leitura(db: Session, leitura: schemas.LeituraCreate):
    db_leitura = models.Leituras(device=leitura.device, leitura=leitura.leitura, timestamp=leitura.timestamp)
    db.add(db_leitura)
    db.commit()
    db.refresh(db_leitura)
    return db_leitura

