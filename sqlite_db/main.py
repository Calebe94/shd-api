from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/leitura", response_model=schemas.Leitura)
def create_leitura(leitura: schemas.LeituraCreate, db: Session = Depends(get_db)):
    return crud.create_leitura(db=db, leitura=leitura)


@app.get("/leitura/{device}", response_model=schemas.Leitura)
def read_leitura(device: int, db: Session = Depends(get_db)):
    leitura = crud.get_leitura(db, device)
    return leitura

