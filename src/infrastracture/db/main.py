from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi


def create_mongo_client(mongo_db_url: str) -> AsyncIOMotorClient:
    return AsyncIOMotorClient(
        mongo_db_url,
        server_api=ServerApi('1')
    )
