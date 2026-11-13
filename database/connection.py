from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import Any, List, Optional
import os
from dotenv import load_dotenv

from models.events import Event
from models.users import User

load_dotenv()

async def initialize_database():
    """Инициализация подключения к MongoDB"""
    database_url = os.getenv("DATABASE_URL", "mongodb://localhost:27017/planner")
    client = AsyncIOMotorClient(database_url)
    await init_beanie(
        database=client.get_default_database(),
        document_models=[Event, User]
    )
    print("MongoDB и Beanie успешно инициализированы!")

class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        des_body = body.model_dump(exclude_unset=True)
        update_query = {"$set": {field: value for field, value in des_body.items()}}
        
        doc = await self.get(id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True