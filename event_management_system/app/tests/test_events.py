from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_home():

    response = client.get("/")

    assert response.status_code == 200



def test_register_user():

    response = client.post(

        "/auth/register",

        json={

            "name": "Test User",

            "email": "testuser@gmail.com",

            "password": "12345",

            "role": "Attendee"

        }

    )


    assert response.status_code in [200, 400]



def test_login():

    response = client.post(

        "/auth/login",

        json={

            "email": "testuser@gmail.com",

            "password": "12345"

        }

    )


    assert response.status_code in [200, 401]



def test_create_event_without_token():

    response = client.post(

        "/api/v1/events/",

        json={

            "event_name": "Python Event",

            "description": "Testing",

            "location": "Chennai",

            "event_date": "2026-07-10T10:00:00",

            "total_seats": 100

        }

    )


    assert response.status_code == 401