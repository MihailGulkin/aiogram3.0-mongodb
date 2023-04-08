from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient

from src.infrastracture.db.repositories import (
    CalculateSalaryStatisticRepository
)


class SalaryRepositoriesMiddleware(BaseMiddleware):
    def __init__(self, client: AsyncIOMotorClient) -> None:
        self.salary_repo = CalculateSalaryStatisticRepository(client=client)

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        data['salary_repo'] = self.salary_repo
        return await handler(event, data)
