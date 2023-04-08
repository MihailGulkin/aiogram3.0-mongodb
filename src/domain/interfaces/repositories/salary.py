from abc import abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient

from src.domain.dto.query import base_pipe_line
from src.domain.dto.salary import Salary
from src.domain.interfaces.repositories.base_repo import BaseRepository


class BaseSalaryAggregateRepository(BaseRepository):
    @abstractmethod
    def __init__(self, *, client: AsyncIOMotorClient):
        super().__init__(client=client)

    @abstractmethod
    async def aggregate_salary(
            self,
            *,
            pipeline: base_pipe_line,
            db_name: str,
            collection: str
    ) -> Salary:
        pass
