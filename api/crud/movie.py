import datetime

from database.movie_schema import CinemaCreate, MovieCreate
from database.sql_models import Cinema, Movie
from sqlalchemy.orm import Session


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Movie).offset(skip).limit(limit).all()


def get_cinema(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cinema).offset(skip).limit(limit).all()


def get_movies_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


def get_cinema_by_id(db: Session, cinema_id: int):
    return db.query(Cinema).filter(Cinema.id == cinema_id).first()


def post_movie(db: Session, new_movie: MovieCreate):
    new_release_date = datetime.strptime(new_movie.release_date, "%d/%m/%y")
    genres_string = ','.join([genre for genre in new_movie.genres])
    db_movie = Movie(name=new_movie.name, length=new_movie.length, release_date=new_release_date,
                     language=new_movie.language, genres=genres_string, poster=new_movie.poster, trailer=new_movie.trailer, description=new_movie.description)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def post_cinema(db: Session, new_cinema: CinemaCreate):
    db_cinema = Cinema(name=new_cinema.name, address=new_cinema.address, postal_code=new_cinema.postal_code,
                       city=new_cinema.city, number_of_auditoriums=new_cinema.number_of_auditoriums)
    db.add(db_cinema)
    db.commit()
    db.refresh(db_cinema)
    return db_cinema
