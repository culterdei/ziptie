from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
add_pagination(app)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


@app.post("/post_author", response_model=schemas.Author)
def post_author(author: schemas.AuthorCreate, db: Session=Depends(get_db)):
    return crud.create_author(db=db, author=author)


@app.post("/post_book", response_model=schemas.Book)
def post_book(book: schemas.BookCreate, db: Session=Depends(get_db)):
    return crud.create_book(db=db, book=book)


@app.get("/books_and_authors/", response_model=Page[schemas.Book])
def get_books_and_authors(db: Session=Depends(get_db)):
    return paginate(db.query(models.Book).outerjoin(models.Author))
