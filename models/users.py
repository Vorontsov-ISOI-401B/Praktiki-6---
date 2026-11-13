from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

class User(Document):
    email: EmailStr
    password: str
    username: Optional[str] = None
    events: Optional[List[Link[Event]]] = []

    class Settings:
        name = "users"

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "student@university.com",
                "password": "strongPassword123",
                "username": "IvanStudent",
            }
        }
    }

class NewUser(BaseModel):
    email: EmailStr
    password: str
    username: str

class UserSignIn(BaseModel):
    email: EmailStr
    password: str