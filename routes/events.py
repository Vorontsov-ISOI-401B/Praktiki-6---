from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId
from database.connection import Database
from models.events import Event, EventUpdate
from models.users import User
from typing import List

event_router = APIRouter(tags=["Events"])
event_database = Database(Event)
user_database = Database(User)

# 1. Создание события (POST)
@event_router.post("/new", status_code=201)
async def create_event(body: Event) -> dict:
    user = await user_database.get(body.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied ID does not exist"
        )
    
    await event_database.save(body)
    return {"message": "Event created successfully"}

# 2. Получение всех событий (GET /)
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

# 3. Получение событий конкретного пользователя (GET /user/{user_id})
@event_router.get("/user/{user_id}", response_model=List[Event])
async def retrieve_user_events(user_id: PydanticObjectId) -> List[Event]:
    # Проверяем существование пользователя
    user = await user_database.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied ID does not exist"
        )
    
    events = await Event.find(Event.user_id == user_id).to_list()
    return events


# 4. Обновление события (PUT /{id})
@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event

# 5. Удаление события (DELETE /{id})
@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    success = await event_database.delete(id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {"message": "Event deleted successfully"}