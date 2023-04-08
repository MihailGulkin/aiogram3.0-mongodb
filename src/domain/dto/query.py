from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class TimeAggregate(Enum):
    hour = 'hour'
    day = 'day'
    month = 'month'


class AggregateQuery(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: TimeAggregate

