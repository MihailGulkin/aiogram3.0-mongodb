import asyncio
import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

load_dotenv('.env')


async def test_server():
    # Replace the placeholder with your Atlas connection string
    uri = f"mongodb+srv://{os.getenv('MONGO_NAME')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('mongo_uri')}/?retryWrites=true&w=majority"
    # Set the Stable API version when creating a new client
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    print(await client.list_database_names())


asyncio.run(test_server())
