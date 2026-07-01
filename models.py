# ============================================================
# models.py
# File ini mendefinisikan "bentuk" tabel di database kita.
# Satu class = satu tabel. Ini yang disebut ORM (Object Relational Mapper):
# kita tulis class Python, SQLAlchemy yang urus SQL-nya.
# ============================================================

from sqlalchemy import Column, Integer, String
from database import Base

# Class User merepresentasikan tabel bernama "users" di database.
# Setiap atribut (id, username, dll) = satu kolom di tabel.
class User(Base):

    # __tablename__ menentukan nama tabel di database
    __tablename__ = "users"

    # Column(Integer, primary_key=True) → kolom angka, ID unik tiap user
    # index=True supaya pencarian berdasarkan ID lebih cepat
    id = Column(Integer, primary_key=True, index=True)

    # Column(String) → kolom teks
    # unique=True → tidak boleh ada username yang sama
    # index=True → pencarian username lebih cepat
    username = Column(String, unique=True, index=True, nullable=False)

    # Email juga harus unik, tidak boleh ada yang sama
    email = Column(String, unique=True, index=True, nullable=False)

    # Password disimpan plain text (teks biasa) untuk tujuan pembelajaran.
    # CATATAN PENTING: Di aplikasi nyata, password HARUS di-hash!
    # Materi hashing akan dibahas di modul Kriptografi nanti.
    password = Column(String, nullable=False)

    # Nama lengkap user, boleh kosong (nullable=True adalah default)
    full_name = Column(String, nullable=True)

    # Nama file foto profil. Kosong kalau belum upload.
    photo = Column(String, nullable=True)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    name = Column(String, nullable=False)

    relationship_name = Column(String)

    phone = Column(String)

    user = relationship("User")