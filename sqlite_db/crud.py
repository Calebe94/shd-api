#This file is part of the SHD distribution (https://gitlab.com/projeto-leitor-hidrometro).
#Copyright (C) 2021 TinyTools
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

