from sqlalchemy import Column, Integer, String, Text
from database import Base

class Buku(Base):
    __tablename__ = "buku"

    id = Column(Integer, primary_key=True, index=True)
    judul = Column(String, index=True)
    penulis = Column(String)
    penerbit = Column(String)
    tahun_terbit = Column(Integer)
    konten = Column(Text)
    iktisar = Column(Text)
