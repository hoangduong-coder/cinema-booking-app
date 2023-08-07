from pydantic import BaseModel
from typing import List


class Film(BaseModel):
    film_id: int
    name: str
    length: int
    release_date: str
    language: str
    genre: List[str]


class Showtime(BaseModel):
    number_of_room: int
    available_seats: List[int]
    film: Film
    start_time: str
