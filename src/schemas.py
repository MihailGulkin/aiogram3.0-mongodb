import json
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ValidationError


class TimeAggregate(Enum):
    hour = 'hour'
    day = 'day'
    month = 'month'


def convert_from_iso_to_datetime(time: str):
    print(time)
    return datetime.fromisoformat(time)


class AggregateQuery(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: TimeAggregate


if __name__ == '__main__':
    json = {
        "dt_from": "2022-09-01T00:00:00",
        "dt_upto": "2022-12-31T23:59:00",
        "group_type": "month"
    }
    try:
        AggregateQuery(
            **json
        )
    except ValidationError:
        print('sdf')
