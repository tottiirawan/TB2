from pydantic import BaseModel

class BukuBase(BaseModel):
    judul: str
    penulis: str
    penerbit: str
    tahun_terbit: int
    konten: str
    iktisar: str

class BukuCreate(BukuBase):
    pass

class Buku(BukuBase):
    id: int

    class Config:
        orm_mode = True
