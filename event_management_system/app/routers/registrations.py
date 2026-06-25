from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from datetime import datetime

from app.database import get_db

from app.models import Registration, Event, User

from app.dependencies import get_current_user, admin_required

from app.email import send_email



router = APIRouter(

    prefix="/events",

    tags=["Registrations"]

)





# REGISTER EVENT

@router.post("/{event_id}/register")

async def register_event(

    event_id: int,

    db: Session = Depends(get_db),

    user: User = Depends(get_current_user)

):


    event = db.query(Event).filter(

        Event.id == event_id

    ).first()



    if not event:

        raise HTTPException(

            status_code=404,

            detail="Event not found"

        )



    if event.available_seats <= 0:

        raise HTTPException(

            status_code=400,

            detail="Seats are full"

        )



    existing = db.query(Registration).filter(

        Registration.event_id == event_id,

        Registration.user_id == user.id

    ).first()



    if existing:

        raise HTTPException(

            status_code=400,

            detail="Already registered"

        )



    registration = Registration(

        event_id=event_id,

        user_id=user.id,

        registration_date=datetime.utcnow()

    )



    event.available_seats -= 1



    db.add(registration)

    db.commit()

    db.refresh(registration)



    # Email confirmation

    await send_email(user.email)



    return {

        "message": "Registration successful",

        "registration_id": registration.id

    }







# VIEW EVENT ATTENDEES (ADMIN ONLY)

@router.get("/{event_id}/attendees")

def get_attendees(

    event_id: int,

    db: Session = Depends(get_db),

    user = Depends(admin_required)

):


    registrations = db.query(Registration).filter(

        Registration.event_id == event_id

    ).all()



    if not registrations:

        raise HTTPException(

            status_code=404,

            detail="No attendees found"

        )


    return registrations







# CANCEL REGISTRATION


@router.delete("/{event_id}/cancel-registration")

def cancel_registration(

    event_id:int,

    db:Session = Depends(get_db),

    user:User = Depends(get_current_user)

):


    registration = db.query(Registration).filter(

        Registration.event_id == event_id,

        Registration.user_id == user.id

    ).first()



    if not registration:


        raise HTTPException(

            status_code=404,

            detail="Registration not found"

        )



    event = db.query(Event).filter(

        Event.id == event_id

    ).first()



    event.available_seats += 1



    db.delete(registration)

    db.commit()



    return {

        "message":"Registration cancelled"

    }