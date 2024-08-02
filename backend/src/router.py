from typing import Annotated
from fastapi import APIRouter, Depends, Form

from src.schemas import UserCreate, UserLogin
from src.repository import UserRepository



router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
async def register(
    user: Annotated[UserCreate, Depends()]
):
    user_id = await UserRepository.add_user(user)
    return {"ok": True, "user": user_id}

@router.post("/login")
async def login(userLogin: Annotated[UserLogin, Form]):
    users = await UserRepository.login_user(userLogin)
    return {"value": users, "token": "HelloSuperSecuredToken"}

@router.get("/home")
async def home():
    users = await UserRepository.get_users()
    return {"result": users}