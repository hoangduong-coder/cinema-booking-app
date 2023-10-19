from typing import List

from pydantic import BaseModel

from api.models import Screening, Seat


class User(BaseModel):
    id: int
    name: str
    phone: str
    email: str


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

