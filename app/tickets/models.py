import uuid
from datetime import datetime, timezone
from enum import StrEnum, auto
from typing import Self

from sqlalchemy import Column, DateTime, Enum, String

from app.db import Base

from .schemas import TicketCreateSchema


class TicketStatus(StrEnum):
    OPEN = auto()
    STALLED = auto()
    CLOSED = auto()


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(TicketStatus), default=TicketStatus.OPEN, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    @classmethod
    def from_schema(cls, ticket: TicketCreateSchema) -> Self:
        return cls(**ticket.model_dump())
