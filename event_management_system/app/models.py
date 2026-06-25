from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from datetime import datetime



class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    email = Column(String, unique=True)

    password = Column(String)

    role = Column(String, default="Attendee")




class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)

    event_name = Column(String)

    description = Column(String)

    location = Column(String)

    event_date = Column(DateTime)

    total_seats = Column(Integer)

    available_seats = Column(Integer)




class Registration(Base):

    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    event_id = Column(
        Integer,
        ForeignKey("events.id")
    )

    registration_date = Column(
        DateTime,
        default=datetime.utcnow
    )




class Ticket(Base):

    __tablename__ = "tickets"


    id = Column(Integer, primary_key=True)

    registration_id = Column(
        Integer,
        ForeignKey("registrations.id")
    )

    ticket_number = Column(
        String,
        unique=True
    )