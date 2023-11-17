from datetime import datetime
from typing import Annotated

from database import SessionLocal, engine
from fastapi import Depends, FastAPI, Path
from models import sql
from sqlalchemy.orm import Session
from util.helper import convert_to_mins

from api.models.movie_models import Cinema, MovieBase

app = FastAPI()
sql.Base.metadata.create_all(bind=engine)

movie_list = {
    1: {
        "name": "Fast X",
        "length": 141,
        "release": "7.5.2023",
        "language": "English",
        "genre": ["Action"]
    },
    2: {
        "name": "Spider-Man: Across the Spider-Verse",
        "length": 140,
        "release": "31.5.2023",
        "language": "English",
        "genre": ["Action", "Adventure", "Animation"]
    },
    3: {
        "name": "Elemental",
        "length": 109,
        "release": "7.7.2023",
        "language": "English",
        "genre": ["Comedy", "Adventure", "Animation", "Family"]
    }
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/all-movie")
async def get_all_movie():
    result = []
    for i in movie_list:
        movie_list[i]["length"] = convert_to_mins(movie_list[i]["length"])
        result.append(movie_list[i])
    return result


@app.get("/get-movie/{search_movie_id}")
async def get_movie_by_id(search_movie_id: int = Path(description="Select ID of your movie:")):
    for movie_id in movie_list:
        if (search_movie_id == movie_id):
            movie_list[search_movie_id]["length"] = convert_to_mins(
                movie_list[search_movie_id]["length"])
            return movie_list[search_movie_id]
    return {"Data": "Not found"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated(Session, Depends(get_db))


@app.post("/add-movie")
async def create_movie(movie: MovieBase, db: db_dependency):
    new_release_date = datetime.strptime(movie.release_date, "%d/%m/%y")
    db_movie = sql.Movie(name=movie.name, length=movie.length, release_date=new_release_date,
                         language=movie.language, genre=movie.genre, poster=movie.poster)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

@app.post("/add-cinema")
async def create_movie(cinema: Cinema, db: db_dependency):
    db_movie = sql.Cinema(name=cinema.name, city=cinema.city)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

@app.post("/add-auditorium/{cinema_id}")
async def create_movie(cinema_id: str, db: db_dependency):
    db_movie = sql.Cinema(name=cinema.name, city=cinema.city)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)