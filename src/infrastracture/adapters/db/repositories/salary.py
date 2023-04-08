from motor.motor_asyncio import AsyncIOMotorClient

from src.domain.dto.query import base_pipe_line
from src.domain.dto.salary import Salary
from src.domain.interfaces.repositories.salary import \
    BaseSalaryAggregateRepository


class CalculateSalaryStatisticRepository(BaseSalaryAggregateRepository):
    def __init__(self, client: AsyncIOMotorClient):
        super().__init__(client=client)

    async def aggregate_salary(
            self,
            *,
            pipeline: base_pipe_line,
            db_name: str,
            collection: str
    ) -> Salary:
        collection = self.client[db_name][collection]
        result = await collection.aggregate(pipeline).to_list(length=None)

        return Salary(
            dataset=[value['sum'] for value in result],
            labels=[value['date'].isoformat() for value in result]
        )
