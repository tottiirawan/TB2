from sqlalchemy.orm import Session
import models, schemas

def create_buku(db: Session, buku: schemas.BukuCreate):
    db_buku = models.Buku(**buku.dict())
    db.add(db_buku)
    db.commit()
    db.refresh(db_buku)
    return db_buku

def get_buku(db: Session, buku_id: int):
    return db.query(models.Buku).filter(models.Buku.id == buku_id).first()

def get_buku_by_judul(db: Session, judul: str):
    return db.query(models.Buku).filter(models.Buku.judul == judul).first()

def get_buku_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Buku).offset(skip).limit(limit).all()

def delete_buku(db: Session, buku_id: int):
    db_buku = db.query(models.Buku).filter(models.Buku.id == buku_id).first()
    if db_buku:
        db.delete(db_buku)
        db.commit()
    return db_buku

def update_buku(db: Session, buku_id: int, buku_update: schemas.BukuCreate):
    db_buku = db.query(models.Buku).filter(models.Buku.id == buku_id).first()
    if db_buku:
        db_buku.judul = buku_update.judul
        db_buku.penulis = buku_update.penulis
        db_buku.penerbit = buku_update.penerbit
        db_buku.tahun_terbit = buku_update.tahun_terbit
        db_buku.konten = buku_update.konten
        db_buku.iktisar = buku_update.iktisar
        db.commit()
        db.refresh(db_buku)
    return db_buku

