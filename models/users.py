from sqlmodel import SQLModel, Field
from typing import Optional, List

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password: str
    username: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "email": "student@university.com",
                "password": "strongPassword123",
                "username": "IvanStudent"
            }
        }
    }

class NewUser(SQLModel):
    email: str
    password: str
    username: str

class UserSignIn(SQLModel):
    email: str
    password: str