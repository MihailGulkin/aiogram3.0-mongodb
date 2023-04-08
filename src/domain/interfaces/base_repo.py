from abc import ABC, abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient

from src.domain.dto.salary import Salary


class BaseRepository(ABC):
    def __init__(self, *, client: AsyncIOMotorClient):
        self.client = client


class BaseSalaryAggregateRepository(BaseRepository):
    @abstractmethod
    def __init__(self, *, client: AsyncIOMotorClient):
        super().__init__(client=client)

    @abstractmethod
    async def aggregate_salary(self) -> Salary:
        pass
