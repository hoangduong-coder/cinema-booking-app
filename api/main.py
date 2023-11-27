from crud.movie import (get_cinema, get_cinema_by_id, get_movies,
                        get_movies_by_id, post_cinema, post_movie)
from database import movie_schema, sql_models
from database.settings import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()
sql_models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/all-movies", response_model=list[movie_schema.Movie])
def read_all_movie(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    movie_list = get_movies(db, skip=skip, limit=limit)
    return movie_list


@app.get("/get-movie/{movie_id}", response_model=movie_schema.Movie)
def read_movie_by_id(movie_id: int, db: Session = Depends(get_db)):
    movie_result = get_movies_by_id(db, movie_id=movie_id)
    if movie_result is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_result


@app.post("/add-movie", response_model=movie_schema.Movie)
def create_movie(movie: movie_schema.MovieCreate, db: Session = Depends(get_db)):
    return post_movie(db, new_movie=movie)


@app.get("/all-cinemas", response_model=list[movie_schema.Cinema])
def read_all_movie(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    cinema_list = get_cinema(db, skip=skip, limit=limit)
    return cinema_list


@app.get("/get-cinema/{cinema_id}", response_model=movie_schema.Movie)
def read_movie_by_id(cinema_id: int, db: Session = Depends(get_db)):
    cinema_result = get_cinema_by_id(db, cinema_id=cinema_id)
    if cinema_result is None:
        raise HTTPException(status_code=404, detail="Cinema not found")
    return cinema_result


@app.post("/add-cinema", response_model=movie_schema.Cinema)
def create_cinema(cinema: movie_schema.CinemaCreate, db: Session = Depends(get_db)):
    return post_cinema(db, new_cinema=cinema)
