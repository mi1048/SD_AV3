from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.post("/users/")
async def create_user(user: User):
    if user_service.get_user(user.username):
        raise HTTPException(
            status_code=400, detail="Username already registered")
    return user_service.create_user(user)

@router.get("/users/{username}")
async def get_user(username: str):
    user = user_service.get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{username}/score")
async def update_score(username: str, score: int):
    user = user_service.update_score(username, score)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user