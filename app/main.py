from contextlib import asynccontextmanager

from fastapi import FastAPI

from .db import Base, engine
from .tickets.routers import router as ticket_router


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Ticket Management API",
    description="Mini API REST de gestion de tickets avec FastAPI",
    version="1.0.0",
    lifespan=lifespan,
)
app.include_router(ticket_router)
