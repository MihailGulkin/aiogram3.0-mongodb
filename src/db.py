import asyncio
import datetime
from bson.json_util import dumps
from dateutil.relativedelta import relativedelta

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
        {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}},
        {"$group": {
            "_id": {
                "year": {"$year": "$dt"},
                "month": {"$month": "$dt"},
                "day": {"$dayOfMonth": "$dt"}
            },
            "total": {"$sum": "$value"}
        }},
        {"$sort": {"_id.year": 1, "_id.month": 1, "_id.day": 1}},
        {"$project": {
            "total": 1,
            "date": {"$dateFromParts": {
                "year": "$_id.year",
                "month": "$_id.month",
                "day": "$_id.day",
                "hour": 0,
                "minute": 0,
                "second": 0,
                "millisecond": 0
            }}
        }}
    ]
    # if group_type == 'day':
    #     pipeline[1]['$group']['_id'] = {
    #         '$dateToString': {'format': f"%Y-%m-%dT00:00:00.000Z",
    #                           'date': '$dt'}}
    # elif group_type == 'hour':
    #     pipeline[1]['$group']['_id'] = {
    #         '$dateToString': {'format': f"%Y-%m-%dT%H:00:00.000Z",
    #                           'date': '$dt'}}

    if group_type == "hour":
        pipeline[1]["$group"]["_id"]["hour"] = {"$hour": "$dt"}
        pipeline[3]["$project"]["date"]["hour"] = "$_id.hour"
    elif group_type == "day":
        pipeline[1]["$group"]["_id"].pop("day")
    elif group_type == "month":
        pipeline[1]["$group"]["_id"].pop("day")

    cursor = collection.aggregate(pipeline)

    async for doc in cursor:
        print(doc)
async def main():
    # задать временной диапазон для фильтрации
    dt_from = datetime.datetime.fromisoformat("2022-09-01T00:00:00")
    dt_upto = datetime.datetime.fromisoformat("2022-12-31T23:59:00")
    group_type = 'month'
    # создать словарь-фильтр

    await aggregate_data(dt_from, dt_upto, group_type)



asyncio.run(main())

# cursor = collection.aggregate([
#     {'$match': filter_},
#     {'$group': group},
#     # {'$project': projection},
#     # {'$sort': {'labels': 1}}
# ])
