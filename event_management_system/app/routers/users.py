from fastapi import APIRouter, Depends

from app.dependencies import get_current_user

from app.models import User



router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.get("/profile")
def profile(

    user: User = Depends(get_current_user)

):

    return {

        "id": user.id,

        "name": user.name,

        "email": user.email,

        "role": user.role

    }