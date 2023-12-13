from typing import Optional

from pydantic import BaseModel

from api.database.movie_schema import Movie


class CinemaBase(BaseModel):
    name: str
    address: str
    postal_code: str
    city: str
    number_of_auditoriums: int
    available: bool


class Cinema(CinemaBase):
    id: int

    class Config:
        orm_mode = True


class CinemaCreate(CinemaBase):
    pass


class CinemaUpdate(BaseModel):
    name: Optional[str] = None
    address:  Optional[str] = None
    postal_code:  Optional[str] = None
    city:  Optional[str] = None
    number_of_auditoriums:  Optional[int] = None
    available: Optional[bool] = None


class ScreeningBase(BaseModel):
    movie: Movie
    cinema: Cinema
    auditorium: int
    start_time: str


class Screening(ScreeningBase):
    id: int

    class Config:
        orm_mode = True


class ScreeningCreate(ScreeningBase):
    pass
