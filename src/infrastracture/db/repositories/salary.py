from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorClient

from src.domain.dto.salary import Salary
from src.domain.interfaces.base_repo import BaseSalaryAggregateRepository


class CalculateSalaryStatisticRepository(BaseSalaryAggregateRepository):
    def __init__(self, client: AsyncIOMotorClient):
        super().__init__(client=client)

    async def aggregate_salary(self) -> Salary:
        print(self.client)
        return Salary(dataset=[33, 23, 23], labels=[
            datetime.fromisoformat('2022-09-01T00:00:00')]
                      )
