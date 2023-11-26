from typing import List, Optional

from pydantic import BaseModel

from api.models import Screening, Seat


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


class TicketType(BaseModel):
    id: int
    type_name: str
    price: float


class Reservation(BaseModel):
    id: int
    screening: Screening
    ticket_type: TicketType
    seat: Seat


class Order(BaseModel):
    id: str
    user: User
    tickets: List[Reservation]
    price: float
