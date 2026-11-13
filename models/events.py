from beanie import Document, PydanticObjectId
from pydantic import BaseModel
from typing import Optional, List

class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    
    user_id: PydanticObjectId

    class Settings:
        name = "events"

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book.",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
                "user_id": "65a1b2c3d4e5f6a7b8c9d0e1"
            }
        }
    }

class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
    user_id: Optional[PydanticObjectId] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Updated FastAPI Book Launch",
                "location": "Hybrid"
            }
        }
    }