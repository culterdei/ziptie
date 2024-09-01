from sqlalchemy.orm import Session

from . import models, schemas


def create_author(db: Session, author: schemas.AuthorCreate):
    author = models.Author(**author.model_dump())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def create_book(db: Session, book: schemas.BookCreate):
    book = models.Book(**book.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book
