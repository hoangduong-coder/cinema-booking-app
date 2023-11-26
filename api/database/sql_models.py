from sqlalchemy import ARRAY, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .settings import Base

# Movie-related SQL models


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    length = Column(Integer)
    release_date = Column(String(20))
    language = Column(String(20))
    genres = Column(ARRAY(String(20)))
    poster = Column(String)
    screening = relationship("Screening", back_populates="movie")


class Cinema(Base):
    __tablename__ = "cinemas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    city = Column(String(50))
    number_of_auditoriums = Column(Integer)

    seat = relationship("Seat", back_populates="cinema")


class Seat(Base):
    __tablename__ = "seats"
    id = Column(String(50), primary_key=True, index=True)
    row = Column(String(2))
    number = Column(Integer)
    special = Column(Boolean)
    auditorium = Column(Integer)
    cinema_id = Column(String(50), ForeignKey("cinemas.id"))

    cinema = relationship("Cinema", back_populates="seat")


class Screening(Base):
    __tablename__ = "screenings"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    auditorium_id = Column(String(50), ForeignKey("auditoriums.id"))
    start_time = Column(String(20))

    movie = relationship("Movie", back_populates="screening")
    auditorium = relationship("Auditorium", back_populates="screening")
    user_reservation = relationship("Reservation", back_populates="screening")

# Human-related SQL models


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    phone = Column(String(50))
    email = Column(String(50))
    reservation = relationship("Reservation", back_populates="user")


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    screening_id = Column(Integer, ForeignKey("screenings.id"))
    ticket_type = Column(String(50))
    seat_code = Column(String(10))
    paid_date = Column(String(20))
    canceled = Column(Boolean)

    user = relationship("User", back_populates="reservation")
    screening = relationship("Screening", back_populates="user_reservation")
