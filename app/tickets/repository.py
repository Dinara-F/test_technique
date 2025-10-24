from fastapi import Depends
from sqlalchemy.orm import Session

from ..db import get_db
from .models import Ticket, TicketStatus
from .schemas import TicketUpdateSchema


class TicketRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, ticket: Ticket) -> Ticket:
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    def find(self) -> list[Ticket]:
        return self.db.query(Ticket).all()

    def get(self, ticket_id: str) -> Ticket | None:
        return self.db.query(Ticket).filter(Ticket.id == ticket_id).first()

    def update(self, ticket_id: str, update: TicketUpdateSchema) -> Ticket | None:
        self.db.query(Ticket).filter(Ticket.id == ticket_id).update(update.model_dump())  # type: ignore[arg-type]
        self.db.commit()

        return self.get(ticket_id)

    def close(self, ticket_id: str) -> Ticket | None:
        ticket = self.get(ticket_id)
        if not ticket:
            return None
        ticket.status = TicketStatus.CLOSED  # type: ignore[assignment]
        self.db.commit()
        self.db.refresh(ticket)
        return ticket
