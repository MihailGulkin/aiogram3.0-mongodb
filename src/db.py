import asyncio
import datetime
from bson.json_util import dumps

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from config import config


async def aggregate_data(dt_from, dt_upto, group_type):
    client = AsyncIOMotorClient(
        config.mongo_db_url.get_secret_value(),
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
        {
            "$group": {
                "_id": {"month": {"$month": '$dt'}},
                "total_amount": {"$sum": "$value"},
                'date': {"$first": "$dt"}
            }
        },
        {
            '$sort': {
                '_id': 1
            }
        }
    ]

    result = await collection.aggregate(pipeline).to_list(length=None)
    dataset = [value['total_amount'] for value in result]
    labels = [value['date'].isoformat() for value in result]
    print({'dataset': dataset, 'labels': labels})


async def main():
    # задать временной диапазон для фильтрации
    dt_from = datetime.datetime.fromisoformat("2022-09-01T00:00:00")
    dt_upto = datetime.datetime.fromisoformat("2022-12-31T23:59:00")
    group_type = 'month'
    # [8177, 8407, 4868, 7706, 8353, 7143, 6062, 11800, 4077, 8820, 4788, 11045, 13048, 2729, 4038, 9888, 7490, 11644, 11232, 12177, 2741, 5341, 8730, 4718, 0]
    # [8177, 8407, 4868, 7706, 8353, 7143, 6062, 11800, 4077, 8820, 4788, 11045, 13048, 2729, 4038, 9888, 7490, 11644, 11232, 12177, 2741, 5341, 8730, 4718]
    await aggregate_data(dt_from, dt_upto, group_type)


asyncio.run(main())

# cursor = collection.aggregate([
#     {'$match': filter_},
#     {'$group': group},
#     # {'$project': projection},
#     # {'$sort': {'labels': 1}}
# ])
