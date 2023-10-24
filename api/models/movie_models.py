from typing import Optional

from pydantic import BaseModel, HttpUrl


class MovieBase(BaseModel):
    name: str
    length: int
    release_date: str
    language: str
    genre: list = []
    poster: Optional[HttpUrl] = None


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class MovieCreate(MovieBase):
    pass


class Cinema(BaseModel):
    id: str
    name: str
    city: str


class Auditorium(BaseModel):
    id: int
    auditorium_number: int
    cinema_id: str


class Screening(BaseModel):
    id: int
    movie: Movie
    auditorium: Auditorium
    start_time: str


class Seat(BaseModel):
    id: str
    auditorium: Auditorium
    row: str
    number: int
    special: bool
