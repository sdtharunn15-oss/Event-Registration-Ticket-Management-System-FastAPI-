from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models import User

from app.schemas import UserCreate, UserLogin

from app.security import (
    hash_password,
    verify_password,
    create_token
)



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)




@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):


    existing = db.query(User).filter(
        User.email == user.email
    ).first()



    if existing:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )



    new_user = User(

        name=user.name,

        email=user.email,

        password=hash_password(
            user.password
        ),

        role=user.role
    )


    db.add(new_user)

    db.commit()

    db.refresh(new_user)



    return {
        "message":"User registered successfully"
    }






@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):


    db_user = db.query(User).filter(
        User.email == user.email
    ).first()



    if not db_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )



    if not verify_password(
        user.password,
        db_user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )



    token = create_token(
        {
            "user_id": db_user.id,
            "role": db_user.role
        }
    )



    return {

        "access_token": token,

        "token_type":"bearer"

    }