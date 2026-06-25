from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):

    name: str
    email: str
    password: str
    role: str = "Attendee"



class UserLogin(BaseModel):

    email: str
    password: str



class UserResponse(BaseModel):

    id: int
    name: str
    email: str
    role: str


    class Config:
        from_attributes = True

        from datetime import datetime


class EventCreate(BaseModel):

    event_name: str

    description: str

    location: str

    event_date: datetime

    total_seats: int



class EventResponse(BaseModel):

    id: int

    event_name: str

    description: str

    location: str

    event_date: datetime

    total_seats: int

    available_seats: int


    class Config:
        from_attributes = True

        class RegistrationResponse(BaseModel):

         id: int

    user_id: int

    event_id: int

    registration_date: datetime


class Config:
        from_attributes = True
        class TicketResponse(BaseModel):

         ticket_number: str

        attendee_name: str
   
        event_name: str

        registration_date: datetime  

        class TicketResponse(BaseModel):

         ticket_number: str

        attendee_name: str

        event_name: str

        registration_date: datetime

        class RegistrationResponse(BaseModel):

         id:int

        user_id:int

        event_id:int

        registration_date:datetime


        class Config:
         from_attributes=True

         


class TicketResponse(BaseModel):

    ticket_number: str

    attendee_name: str

    event_name: str

    registration_date: datetime