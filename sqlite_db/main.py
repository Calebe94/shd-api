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

from typing import List

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/db",
    tags=["leituras"],
    responses={404: {"description": "Not found"}},
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/leitura", response_model=schemas.Leitura)
def create_leitura(leitura: schemas.LeituraCreate, db: Session = Depends(get_db)):
    return crud.create_leitura(db=db, leitura=leitura)


@router.get("/leitura/{device}", response_model=schemas.Leitura)
def read_leitura(device: int, db: Session = Depends(get_db)):
    leitura = crud.get_leitura(db, device)
    return leitura

