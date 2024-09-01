from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.dialects.mysql import SMALLINT, DATE
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, nullable=False)
    year = Column(SMALLINT)
    short_desc = Column(String(255))
    original_lang = Column(String(30))
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    is_nobel_prize_winner = Column(Boolean, default=False)
    date_of_birth = Column(DATE)
    date_of_death = Column(DATE)
    books = relationship("Book", back_populates="author")
