from pydantic import BaseModel
from typing import List
from api.models import Film
from enum import Enum


class TicketType(Enum):
    REGULAR: 1
    CHILD: 2
    STUDENT: 3
    WHEELCHAIR: 4


class Ticket(BaseModel):
    film: Film
    date_time: str
    type_of_ticket: TicketType
    quantity: int
    price: float


class Order(BaseModel):
    name: str
    email: str
    phone: str
    tickets: List[Ticket]
