from typing import Any

from src.domain.dto.query import AggregateQuery, base_pipe_line, TimeAggregate


class QuerySalaryBuilder:
    def __init__(self, aggregate_data: AggregateQuery):
        self.aggregate_data = aggregate_data

    def _get_date_format(self) -> str:
        if self.aggregate_data.group_type == TimeAggregate.day:
            return '$dayOfMonth'
        if self.aggregate_data.group_type == TimeAggregate.hour:
            return "$hour"
        if self.aggregate_data.group_type == TimeAggregate.week:
            return "$week"
        return "$month"

    def _get_match(self) -> dict[str, Any]:
        return {
            "dt": {
                "$gte": self.aggregate_data.dt_from,
                "$lte": self.aggregate_data.dt_upto
            }}

    def _get_group(self) -> dict[str, Any]:
        return {
            "_id": {self._get_date_format(): "$dt"},
            "sum": {"$sum": "$value"},
            'date': {'$first': '$dt'}
        }

    def get_pipe_line(self) -> base_pipe_line:
        return [{"$match": self._get_match()},
                {"$group": self._get_group()},
                {"$sort": {"_id": 1}},
                ]
