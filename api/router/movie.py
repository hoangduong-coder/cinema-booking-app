from crud import movie
from database import movie_schema
from database.settings import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/movie", tags=["movie"])


@router.get("/all", response_model=list[movie_schema.Movie])
def read_all_movie(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movie_list = movie.get_movies(db, skip=skip, limit=limit)
    return movie_list


@router.get("/{movie_id}", response_model=movie_schema.Movie)
def read_movie_by_id(movie_id: int, db: Session = Depends(get_db)):
    movie_result = movie.get_movies_by_id(db, movie_id=movie_id)
    if movie_result is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_result


@router.post("/new", response_model=movie_schema.Movie)
def create_movie(movie: movie_schema.MovieCreate, db: Session = Depends(get_db)):
    return movie.post_movie(db, new_movie=movie)


@router.put("/update/{movie_id}", response_model=movie_schema.MovieUpdate)
def update_movie(movie_id: int, db: Session = Depends(get_db), change_args: movie_schema.MovieUpdate = {}):
    new_change_args = {key: value for key,
                       value in change_args.dict().items() if value is not None}
    return movie.change_movie(db, movie_id, **new_change_args)


@router.delete("/delete/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    return movie.remove_movie(db, movie_id)
