""" Pydantic Schemas """

from fastapi import Form
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    login: str

class UserCreate(UserBase):
    password: str

class TestLoginForm(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    login: str
    password: str

    @classmethod
    def as_form(
        cls,
        login: str = Form(...),
        password: str = Form(...)
    ):
        return cls(login=login, password=password)