Event Registration & Ticket Management System

Project Overview

The Event Registration & Ticket Management System is a backend application built using FastAPI.
It allows users to register, login, create events, view events, update events, delete events, and manage event-related operations securely using JWT authentication.

Tech Stack

* Python 3.9+
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite / PostgreSQL
* JWT Authentication
* Uvicorn

Features

Authentication

* User registration
* User login
* JWT token-based authentication
* Secure API access

User Management

* View user profile
* Manage authenticated users

Event Management

* Create events
* View all events
* Update event details
* Delete events

Project Structure


event_management_system/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── dependencies.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── events.py
│
├── requirements.txt
├── README.md
└── database.db


Installation & Setup

1. Clone the repository


git clone <repository-url>


2. Create virtual environment


python -m venv venv

Activate:

Windows:

venv\Scripts\activate


Linux/Mac:


source venv/bin/activate


3. Install dependencies


pip install -r requirements.txt

Running the Application

Start FastAPI server:


uvicorn app.main:app --reload

Application runs at:


http://127.0.0.1:8000


Swagger API Documentation:


http://127.0.0.1:8000/docs


API Endpoints

Authentication

| Method | Endpoint       | Description   |
| ------ | -------------- | ------------- |
| POST   | /auth/register | Register user |
| POST   | /auth/login    | Login user    |

Users

| Method | Endpoint              | Description      |
| ------ | --------------------- | ---------------- |
| GET    | /api/v1/users/profile | Get user profile |

Events

| Method | Endpoint                  | Description    |
| ------ | ------------------------- | -------------- |
| POST   | /api/v1/events/           | Create event   |
| GET    | /api/v1/events/           | Get all events |
| PUT    | /api/v1/events/{event_id} | Update event   |
| DELETE | /api/v1/events/{event_id} | Delete event   |

Authentication Flow

1. User registers account.
2. User logs in.
3. Server generates JWT access token.
4. Token is used to access protected APIs.

Example:


Authorization: Bearer <access_token>


Database

The project uses SQLAlchemy ORM for database operations.

Main tables:

Users Table

* id
* username
* email
* password

Events Table

* id
* title
* description
* date
* location
* created_by

Future Improvements

* Ticket booking system
* Payment integration
* Event reminders
* Admin dashboard
* Email notifications

Author

Tharun
