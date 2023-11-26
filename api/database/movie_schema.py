from pydantic import BaseModel, HttpUrl


class MovieBase(BaseModel):
    name: str
    length: int
    release_date: str
    language: str
    genres: list = []
    description: str
    trailer: HttpUrl
    poster: HttpUrl  # temporary save to a cloud storage, find a way to solve later


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class MovieCreate(MovieBase):
    pass


class CinemaBase(BaseModel):
    name: str
    address: str
    postal_code: str
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
    cinema: Cinema
    auditorium: int
    start_time: str


class Screening(ScreeningBase):
    id: int

    class Config:
        orm_mode = True


class ScreeningCreate(ScreeningBase):
    pass
