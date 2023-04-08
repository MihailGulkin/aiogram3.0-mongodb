from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel


class TimeAggregate(Enum):
    hour = 'hour'
    day = 'day'
    week = "week"
    month = 'month'


class AggregateQuery(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: TimeAggregate


base_pipe_line = list[dict[str, Any]]
