import pprint

from src.domain.dto.db import MongoDBCollections
from src.domain.dto.query import AggregateQuery
from src.domain.dto.salary import Salary
from src.domain.interfaces.repositories.salary import (
    BaseSalaryAggregateRepository
)
from src.domain.interfaces.usecase import BaseSalaryUseCase
from src.infrastracture.adapters.queries.salary import QuerySalaryBuilder


class SalaryQueryUseCase(BaseSalaryUseCase):
    def __init__(
            self,
            *,
            salary_repo: BaseSalaryAggregateRepository,
            db_collection: MongoDBCollections
    ):
        super().__init__(salary_repo)
        self.mongo_info = db_collection

    async def __call__(self, aggregate_query: AggregateQuery) -> Salary:
        pipeline = QuerySalaryBuilder(aggregate_query).get_pipe_line()

        return await self.salary_repo.aggregate_salary(
            pipeline=pipeline,
            db_name=self.mongo_info.db,
            collection=self.mongo_info.collections
        )
