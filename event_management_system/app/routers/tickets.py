from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from uuid import uuid4

from app.database import get_db

from app.models import (
    Ticket,
    Registration,
    User,
    Event
)
from app.schemas import TicketResponse


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)




@router.get("/{registration_id}", response_model=TicketResponse)
def generate_ticket(

    registration_id:int,

    db:Session = Depends(get_db)

):


    registration = db.query(
        Registration
    ).filter(
        Registration.id == registration_id
    ).first()



    if not registration:

        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )



    existing_ticket = db.query(
        Ticket
    ).filter(
        Ticket.registration_id == registration_id
    ).first()



    if existing_ticket:

        ticket = existing_ticket


    else:


        ticket = Ticket(

            registration_id = registration_id,

            ticket_number = "TKT-" + str(uuid4())[:8]

        )


        db.add(ticket)

        db.commit()

        db.refresh(ticket)





    user = db.query(User).filter(
        User.id == registration.user_id
    ).first()



    event = db.query(Event).filter(
        Event.id == registration.event_id
    ).first()



    return {

        "ticket_number": ticket.ticket_number,

        "attendee_name": user.name,

        "event_name": event.event_name,

        "registration_date": registration.registration_date

    }