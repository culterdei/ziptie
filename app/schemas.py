from pydantic import BaseModel, field_validator, constr


class BookCreate(BaseModel):
    title: str
    year: int | None = None
    short_desc: str | None = None
    original_lang: str
    author_id: int | None = None


class AuthorCreate(BaseModel):
    name: str
    is_nobel_prize_winner: bool | None = None
    date_of_birth: constr(pattern=r'^\d{1,4}-\d{1,2}-\d{1,2}$') | None = None
    date_of_death: constr(pattern=r'^\d{1,4}-\d{1,2}-\d{1,2}$') | None = None


class Author(AuthorCreate):
    id: int


    @field_validator('date_of_birth', 'date_of_death', mode="before")
    def return_as_str(cls, date):
        if date:
            return date.strftime("%Y-%m-%d")
        return None

    class Config:
        orm_model = True


class Book(BookCreate):
    id: int
    author: Author | None

    class Config:
        orm_mode = True
