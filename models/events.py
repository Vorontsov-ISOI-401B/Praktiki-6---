from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "id": 1,
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }]
        }
    }