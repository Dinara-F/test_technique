from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from .models import Ticket
from .repository import TicketRepository
from .schemas import TicketCreateSchema, TicketSchema, TicketUpdateSchema

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/", status_code=201, response_model=TicketSchema)
def create_ticket(
    ticket: TicketCreateSchema, repo: TicketRepository = Depends(TicketRepository)
) -> TicketSchema:
    return repo.create(Ticket.from_schema(ticket))


@router.get("/", response_model=list[TicketSchema])
def find_tickets(
    repo: TicketRepository = Depends(TicketRepository),
) -> list[TicketSchema]:
    return repo.find()


@router.get("/{ticket_id}", response_model=TicketSchema)
def get_ticket(
    ticket_id: UUID, repo: TicketRepository = Depends(TicketRepository)
) -> TicketSchema:
    ticket = repo.get(str(ticket_id))
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.put("/{ticket_id}", response_model=TicketSchema)
def update_ticket(
    ticket_id: UUID,
    update: TicketUpdateSchema,
    repo: TicketRepository = Depends(TicketRepository),
) -> TicketSchema:
    ticket = repo.update(str(ticket_id), update)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.patch("/{ticket_id}/close", response_model=TicketSchema)
def close_ticket(
    ticket_id: UUID, repo: TicketRepository = Depends(TicketRepository)
) -> TicketSchema:
    ticket = repo.close(str(ticket_id))
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket
