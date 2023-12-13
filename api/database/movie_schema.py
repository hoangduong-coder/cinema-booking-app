from typing import Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    length: int
    release_date: str
    language: str
    genres: str
    description: str
    trailer: str
    poster: str  # temporary save to a cloud storage, find a way to solve later


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    name: Optional[str] = None
    length: Optional[int] = None
    release_date: Optional[str] = None
    language: Optional[str] = None
    genres: Optional[str] = None
    description: Optional[str] = None
    trailer: Optional[str] = None
    poster: Optional[str] = None
