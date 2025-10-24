from app.tickets.models import Ticket, TicketStatus
from app.tickets.repository import TicketRepository
from app.tickets.schemas import (
    TicketCreateSchema,
    TicketStatusSchema,
    TicketUpdateSchema,
)


def test_create_ticket(repo: TicketRepository) -> None:
    ticket = repo.create(
        Ticket.from_schema(TicketCreateSchema(title="First", description="Test first"))
    )
    assert ticket.id is not None
    assert ticket.title == "First"
    assert ticket.description == "Test first"
    assert ticket.status == TicketStatus.OPEN


def test_find(repo: TicketRepository) -> None:
    repo.create(
        Ticket.from_schema(TicketCreateSchema(title="First", description="Test first"))
    )
    repo.create(
        Ticket.from_schema(
            TicketCreateSchema(title="Second", description="Test second")
        )
    )
    tickets = repo.find()
    assert len(tickets) == 2


def test_get_by_id(repo: TicketRepository) -> None:
    t = repo.create(
        Ticket.from_schema(
            TicketCreateSchema(title="Get", description="Test get by id")
        )
    )
    ticket = repo.get(str(t.id))
    assert ticket
    assert ticket.title == "Get"


def test_update(repo: TicketRepository) -> None:
    t = repo.create(
        Ticket.from_schema(
            TicketCreateSchema(title="Update", description="Test update")
        )
    )
    update = TicketUpdateSchema(
        title="New", description="desc2", status=TicketStatusSchema.STALLED
    )
    ticket = repo.update(str(t.id), update)
    assert ticket
    assert ticket.title == "New"
    assert ticket.status == TicketStatus.STALLED
    assert t.created_at == ticket.created_at


def test_close(repo: TicketRepository) -> None:
    t = repo.create(
        Ticket.from_schema(TicketCreateSchema(title="Close", description="Test close"))
    )
    ticket = repo.close(str(t.id))
    assert ticket
    assert ticket.status == TicketStatus.CLOSED
