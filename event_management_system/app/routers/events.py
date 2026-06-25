from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from datetime import datetime

from app.database import get_db

from app.models import Event

from app.schemas import EventCreate, EventResponse

from app.dependencies import admin_required



router = APIRouter(
    prefix="/events",
    tags=["Events"]
)



# CREATE EVENT (ADMIN)

@router.post("/", response_model=EventResponse)
def create_event(

    event: EventCreate,

    db: Session = Depends(get_db),

    user = Depends(admin_required)

):

    if event.event_date <= datetime.now():

        raise HTTPException(
            status_code=400,
            detail="Event date must be future"
        )


    if event.total_seats <= 0:

        raise HTTPException(
            status_code=400,
            detail="Seats must be greater than 0"
        )


    new_event = Event(

        event_name=event.event_name,

        description=event.description,

        location=event.location,

        event_date=event.event_date,

        total_seats=event.total_seats,

        available_seats=event.total_seats

    )


    db.add(new_event)

    db.commit()

    db.refresh(new_event)


    return new_event





# GET EVENTS

@router.get("/", response_model=list[EventResponse])
def get_events(

    location: str = None,

    date: str = None,

    status: str = None,

    page: int = 1,

    limit: int = 10,

    db: Session = Depends(get_db)

):


    query = db.query(Event)



    # Filter by location

    if location:

        query = query.filter(
            Event.location == location
        )



    # Filter by date

    if date:

        query = query.filter(
            Event.event_date.like(
                f"{date}%"
            )
        )



    # Upcoming events

    if status == "upcoming":

        query = query.filter(
            Event.event_date > datetime.now()
        )



    # Pagination

    skip = (page - 1) * limit


    events = query.offset(
        skip
    ).limit(
        limit
    ).all()



    return events

    return db.query(Event).all()





# GET SINGLE EVENT

@router.get("/", response_model=list[EventResponse])
def get_events(

    location: str = None,

    date: str = None,

    status: str = None,

    page: int = 1,

    limit: int = 10,

    db: Session = Depends(get_db)

):

    query = db.query(Event)


    if location:
        query = query.filter(
            Event.location == location
        )


    if date:
        query = query.filter(
            Event.event_date.like(
                f"{date}%"
            )
        )


    if status == "upcoming":

        query = query.filter(
            Event.event_date > datetime.now()
        )


    skip = (page - 1) * limit


    return query.offset(
        skip
    ).limit(
        limit
    ).all()

    event = db.query(Event).filter(
        Event.id == event_id
    ).first()


    if not event:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )


    return event





# UPDATE EVENT (ADMIN)

@router.put("/{event_id}", response_model=EventResponse)
def update_event(

    event_id:int,

    event_data:EventCreate,

    db:Session = Depends(get_db),

    user = Depends(admin_required)

):

    event = db.query(Event).filter(
        Event.id == event_id
    ).first()


    if not event:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )


    event.event_name = event_data.event_name

    event.description = event_data.description

    event.location = event_data.location

    event.event_date = event_data.event_date

    event.total_seats = event_data.total_seats

    event.available_seats = event_data.total_seats


    db.commit()

    db.refresh(event)


    return event





# DELETE EVENT (ADMIN)

@router.delete("/{event_id}")
def delete_event(

    event_id:int,

    db:Session = Depends(get_db),

    user = Depends(admin_required)

):

    event = db.query(Event).filter(
        Event.id == event_id
    ).first()


    if not event:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )


    db.delete(event)

    db.commit()


    return {
        "message":"Event deleted"
    }


@router.get("/{event_id}", response_model=EventResponse)
def get_event(

    event_id:int,

    db:Session = Depends(get_db)

):

    event = db.query(Event).filter(
        Event.id == event_id
    ).first()


    if not event:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )


    return event