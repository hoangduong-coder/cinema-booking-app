from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .settings import Base

# Movie-related SQL models


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    length = Column(Integer)
    release_date = Column(String(20))
    language = Column(String(20))
    genres = Column(String)
    poster = Column(String)
    trailer = Column(String)
    description = Column(String)

    screening = relationship("Screening", back_populates="movie")


class Cinema(Base):
    __tablename__ = "cinemas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    city = Column(String(50))
    address = Column(String)
    postal_code = Column(String(10))
    number_of_auditoriums = Column(Integer)

    screening = relationship("Screening", back_populates="cinema")


class Screening(Base):
    __tablename__ = "screenings"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    auditorium = Column(Integer)
    start_time = Column(DateTime)
    cinema_id = Column(Integer, ForeignKey("cinemas.id"))

    movie = relationship("Movie", back_populates="screening")
    cinema = relationship("Cinema", back_populates="screening")
    booking = relationship("Booking", back_populates="screening")


# Human-related SQL models


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    phone = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))

    booking = relationship("Booking", back_populates="user")


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey("screenings.id"))
    ticket_type = Column(String(50))
    seat = Column(String())
    user_id = Column(Integer, ForeignKey("users.id"))
    paid_datetime = Column(DateTime, server_default=func.now())

    screening = relationship("Screening", back_populates="booking")
    user = relationship("User", back_populates="booking")
