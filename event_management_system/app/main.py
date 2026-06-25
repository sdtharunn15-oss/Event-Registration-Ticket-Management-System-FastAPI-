from fastapi import FastAPI

from app.database import Base, engine

import app.models
from app.routers import auth
from app.routers import events
from app.routers import registrations
from app.routers import tickets
from app.routers import users
app = FastAPI(
    title="Event Registration & Ticket Management System"
)



Base.metadata.create_all(
    bind=engine
)
app.include_router(
    auth.router
)

app.include_router(
    users.router,
    prefix="/api/v1"
)

app.include_router(
    events.router,
    prefix="/api/v1"
)

app.include_router(
    registrations.router,
    prefix="/api/v1"
)

app.include_router(
    tickets.router,
    prefix="/api/v1"
)
@app.get("/")
def home():

    return {
        "message":"Event Management API Running"
    }