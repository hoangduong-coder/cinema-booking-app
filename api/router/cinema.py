from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.crud import cinema
from api.database.settings import get_db

from ..database import cinema_schema

router = APIRouter(prefix="/cinema", tags=["cinema"])


@router.get("/all", response_model=list[cinema_schema.Cinema])
def read_all_cinemas(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    cinema_list = cinema.get_cinema(db, skip=skip, limit=limit)
    return cinema_list


@router.get("/{cinema_id}", response_model=cinema_schema.Cinema)
def read_cinema_by_id(cinema_id: int, db: Session = Depends(get_db)):
    cinema_result = cinema.get_cinema_by_id(db, cinema_id=cinema_id)
    if cinema_result is None:
        raise HTTPException(status_code=404, detail="Cinema not found")
    return cinema_result


@router.post("/add", response_model=cinema_schema.Cinema)
def create_cinema(cinema: cinema_schema.CinemaCreate, db: Session = Depends(get_db)):
    return cinema.post_cinema(db, new_cinema=cinema)


@router.put("/update/{cinema_id}", response_model=cinema_schema.CinemaUpdate)
def update_movie(cinema_id: int, db: Session = Depends(get_db), change_args: cinema_schema.CinemaUpdate = {}):
    new_change_args = {key: value for key,
                       value in change_args.dict().items() if value is not None}
    return cinema.change_cinema(db, cinema_id, **new_change_args)
