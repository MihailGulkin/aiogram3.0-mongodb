from abc import ABC
from typing import Any

from src.domain.dto.salary import Salary
from src.domain.interfaces.repositories.salary import (
    BaseSalaryAggregateRepository
)


class BaseSalaryUseCase(ABC):
    def __init__(self, salary_repo: BaseSalaryAggregateRepository) -> None:
        self.salary_repo = salary_repo

    async def __call__(self, *args, **kwargs) -> Salary:
        pass
