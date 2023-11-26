from enum import Enum
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    phone: str
    email: str


class UserCreate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class TicketType(str, Enum):
    normal = 'NORMAL'
    children = 'CHILDREN'
    premium = 'PREMIUM'
    disability = 'DISABILITY'


class BookingBase(BaseModel):
    id: int
    screening_id: int
    ticket_type: TicketType
    seat: str
    user: User
    paid_datetime: str


class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True


class BookingCreate(BookingBase):
    pass
