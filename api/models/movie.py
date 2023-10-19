from typing import List

from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    name: str
    length: int
    release_date: str
    language: str
    genre: List[str]
    director: str
    cast: List[str]


class Auditorium(BaseModel):
    id: int
    auditorium_number: int
    seats_amount: int


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
