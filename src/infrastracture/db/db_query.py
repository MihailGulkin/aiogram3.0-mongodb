import asyncio
import datetime
from bson.json_util import dumps

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.config import get_settings


async def aggregate_data(dt_from, dt_upto, group_type):
    client = AsyncIOMotorClient(
        get_settings().MONGO_DB_URL.get_secret_value(),
        server_api=ServerApi('1')
    )
    db = client['sampleDB']
    collection = db['sample_collection']
    pipeline = [
        {
            "$match": {
                "dt": {"$gte": dt_from, "$lte": dt_upto}
            }
        },
    ]

    result = await collection.aggregate(pipeline).to_list(length=None)
    print(sum([value['value'] for value in result]))

async def main():
    # задать временной диапазон для фильтрации
    dt_from = datetime.datetime.fromisoformat("2022-12-01T00:00:00")
    dt_upto = datetime.datetime.fromisoformat("2023-01-01T23:59:00")
    group_type = 'month'
    await aggregate_data(dt_from, dt_upto, group_type)


asyncio.run(main())

# cursor = collection.aggregate([
#     {'$match': filter_},
#     {'$group': group},
#     # {'$project': projection},
#     # {'$sort': {'labels': 1}}
# ])