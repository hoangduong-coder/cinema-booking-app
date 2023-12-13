from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.database.cinema_schema import CinemaCreate
from api.database.sql_models import Cinema


def get_cinema(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cinema).offset(skip).limit(limit).all()


def get_cinema_by_id(db: Session, cinema_id: int):
    return db.query(Cinema).filter(Cinema.id == cinema_id).first()


def post_cinema(db: Session, new_cinema: CinemaCreate):
    db_cinema = Cinema(name=new_cinema.name, address=new_cinema.address, postal_code=new_cinema.postal_code,
                       city=new_cinema.city, number_of_auditoriums=new_cinema.number_of_auditoriums)
    db.add(db_cinema)
    db.commit()
    db.refresh(db_cinema)
    return db_cinema


def change_cinema(db: Session, movie_id: int, **change_args):
    selected_cinema = db.query(Cinema).filter(Cinema.id == movie_id).first()
    if selected_cinema is None:
        raise HTTPException(
            status_code=404, detail=f"Cinema with id:{movie_id} is not found or has been deleted")
    for key, new_value in change_args.items():
        if hasattr(selected_cinema, key):
            setattr(selected_cinema, key, new_value)
    db.commit()
    return selected_cinema
