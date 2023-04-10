from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.application.ports.usecase.salary import SalaryQueryUseCase
from src.presentation.di.container import container
from src.presentation.di.providers.services import get_salary_usecase


class SalaryRepositoriesMiddleware(BaseMiddleware):
    def __init__(
            self,
            salary_usecase: SalaryQueryUseCase = container.container.resolve(
                get_salary_usecase
            )
    ) -> None:
        self.salary_usecase = salary_usecase

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        data['salary_usecase'] = self.salary_usecase
        return await handler(event, data)
