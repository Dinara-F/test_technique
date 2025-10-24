from datetime import datetime
from enum import StrEnum, auto
from uuid import UUID

from pydantic import BaseModel


class TicketStatusSchema(StrEnum):
    OPEN = auto()
    STALLED = auto()
    CLOSED = auto()


class TicketCreateSchema(BaseModel):
    title: str
    description: str


class TicketUpdateSchema(TicketCreateSchema):
    status: TicketStatusSchema


class TicketSchema(TicketUpdateSchema):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
