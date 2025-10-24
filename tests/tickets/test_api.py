from datetime import datetime, timezone
from uuid import uuid4

from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from app.main import app
from app.tickets.models import Ticket, TicketStatus
from app.tickets.repository import TicketRepository

client = TestClient(app)


def test_create_ticket(mocker: MockerFixture) -> None:
    ticket = Ticket(
        id=str(uuid4()),
        title="Test",
        description="Mocked",
        status=TicketStatus.OPEN,
        created_at=datetime.now(timezone.utc),
    )
    mocker.patch.object(TicketRepository, "create", return_value=ticket)
    response = client.post("/tickets/", json={"title": "Test", "description": "Mocked"})
    assert response.status_code == 201
    assert response.json()
    assert response.json()["title"] == "Test"


def test_create_invalid_ticket() -> None:
    response = client.post("/tickets/", json={"description": "Mocked"})
    assert response.status_code == 422


def test_find_tickets(mocker: MockerFixture) -> None:
    ticket = Ticket(
        id=str(uuid4()),
        title="Test",
        description="Mocked",
        status=TicketStatus.OPEN,
        created_at=datetime.now(timezone.utc),
    )
    mocker.patch.object(TicketRepository, "find", return_value=[ticket])
    response = client.get("/tickets/")
    assert response.status_code == 200
    assert response.json()
    assert len(response.json()) == 1


def test_get_ticket(mocker: MockerFixture) -> None:
    ticket = Ticket(
        id=str(uuid4()),
        title="Test",
        description="Mocked",
        status=TicketStatus.OPEN,
        created_at=datetime.now(timezone.utc),
    )
    mocker.patch.object(TicketRepository, "get", return_value=ticket)
    response = client.get("/tickets/12345678-1234-1234-1234-123456789abc")
    assert response.status_code == 200
    assert response.json()


def test_get_ticket_nonexistent(mocker: MockerFixture) -> None:
    mocker.patch.object(TicketRepository, "get", return_value=None)
    response = client.get("/tickets/12345678-1234-1234-1234-123456789abc")
    assert response.status_code == 404


def test_update_ticket(mocker: MockerFixture) -> None:
    ticket = Ticket(
        id=str(uuid4()),
        title="Test",
        description="Mocked",
        status=TicketStatus.OPEN,
        created_at=datetime.now(timezone.utc),
    )
    mocker.patch.object(TicketRepository, "update", return_value=ticket)
    response = client.put(
        "/tickets/12345678-1234-1234-1234-123456789abc",
        json={"title": "Updated", "description": "Updated desc", "status": "stalled"},
    )
    assert response.status_code == 200
    assert response.json()


def test_update_invalid() -> None:
    response = client.put(
        "/tickets/12345678-1234-1234-1234-123456789abc",
        json={"title": "Updated", "description": "Updated desc"},
    )
    assert response.status_code == 422


def test_update_nonexistent(mocker: MockerFixture) -> None:
    mocker.patch.object(TicketRepository, "update", return_value=None)
    response = client.put(
        "/tickets/12345678-1234-1234-1234-123456789abc",
        json={"title": "Updated", "description": "Updated desc", "status": "stalled"},
    )
    assert response.status_code == 404


def test_close_ticket(mocker: MockerFixture) -> None:
    ticket = Ticket(
        id=str(uuid4()),
        title="Test",
        description="Mocked",
        status=TicketStatus.OPEN,
        created_at=datetime.now(timezone.utc),
    )
    mocker.patch.object(TicketRepository, "close", return_value=ticket)
    response = client.patch(
        "/tickets/12345678-1234-1234-1234-123456789abc/close", json={}
    )
    assert response.status_code == 200
    assert response.json()


def test_close_nonexistent(mocker: MockerFixture) -> None:
    mocker.patch.object(TicketRepository, "close", return_value=None)
    response = client.patch(
        "/tickets/12345678-1234-1234-1234-123456789abc/close", json={}
    )
    assert response.status_code == 404
