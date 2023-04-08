from abc import ABC

from motor.motor_asyncio import AsyncIOMotorClient


class BaseRepository(ABC):
    def __init__(self, *, client: AsyncIOMotorClient):
        self.client = client
