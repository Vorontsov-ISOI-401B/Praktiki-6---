from sqlmodel import SQLModel, Field, Column, Relationship
from typing import Optional, List
from sqlalchemy import JSON

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str
    
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book.",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
                "user_id": 1
            }
        }
    }

class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
    user_id: Optional[int] = None