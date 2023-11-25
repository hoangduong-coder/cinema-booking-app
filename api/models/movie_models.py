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


class CinemaBase(BaseModel):
    name: str
    city: str
    number_of_auditoriums: int


class Cinema(CinemaBase):
    id: int

    class Config:
        orm_mode = True


class CinemaCreate(CinemaBase):
    pass


class ScreeningBase(BaseModel):
    movie: Movie
    cinema_id: int
    auditorium: int
    start_time: str


class Screening(ScreeningBase):
    id: int

    class Config:
        orm_mode = True


class ScreeningCreate(ScreeningBase):
    pass


class Seat(BaseModel):
    id: str
    cinema_id: int
    auditorium: int
    row: str
    number: int
    special: bool
