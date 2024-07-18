import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas, database

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/buku/", response_model=schemas.Buku)
def create_buku(buku: schemas.BukuCreate, db: Session = Depends(database.get_db)):
    db_buku = crud.get_buku_by_judul(db, judul=buku.judul)
    if db_buku:
        logger.error(f"Buku {buku.judul} already registered")
        raise HTTPException(status_code=400, detail="Buku already registered")
    logger.info(f"Creating buku {buku.judul}")
    return crud.create_buku(db=db, buku=buku)

@app.get("/buku/{buku_id}", response_model=schemas.Buku)
def read_buku(buku_id: int, db: Session = Depends(database.get_db)):
    db_buku = crud.get_buku(db, buku_id=buku_id)
    if db_buku is None:
        logger.error(f"Buku with id {buku_id} not found")
        raise HTTPException(status_code=404, detail="Buku not found")
    logger.info(f"Reading buku with id {buku_id}")
    return db_buku

@app.get("/buku/", response_model=List[schemas.Buku])
def read_buku_all(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    logger.info("Fetching all buku")
    buku = crud.get_buku_all(db, skip=skip, limit=limit)
    return buku

@app.delete("/buku/{buku_id}", response_model=schemas.Buku)
def delete_buku(buku_id: int, db: Session = Depends(database.get_db)):
    db_buku = crud.get_buku(db, buku_id=buku_id)
    if db_buku is None:
        logger.error(f"Buku with id {buku_id} not found")
        raise HTTPException(status_code=404, detail="Buku not found")
    logger.info(f"Deleting buku with id {buku_id}")
    return crud.delete_buku(db=db, buku_id=buku_id)

@app.put("/buku/{buku_id}", response_model=schemas.Buku)
def update_buku(buku_id: int, buku: schemas.BukuCreate, db: Session = Depends(database.get_db)):
    db_buku = crud.get_buku(db, buku_id=buku_id)
    if db_buku is None:
        logger.error(f"Buku with id {buku_id} not found")
        raise HTTPException(status_code=404, detail="Buku not found")
    logger.info(f"Updating buku with id {buku_id}")
    return crud.update_buku(db=db, buku_id=buku_id, buku_update=buku)
