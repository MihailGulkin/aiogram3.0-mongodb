from motor.motor_asyncio import AsyncIOMotorClient

from src.application.ports.usecase.salary import SalaryQueryUseCase
from src.domain.dto.db import MongoDBCollections
from src.infrastracture.adapters.db.repositories import \
    CalculateSalaryStatisticRepository


def get_salary_usecase(client: AsyncIOMotorClient) -> SalaryQueryUseCase:
    return SalaryQueryUseCase(
        salary_repo=CalculateSalaryStatisticRepository(client=client),
        db_collection=MongoDBCollections(
            db='sampleDB',
            collections='sample_collection'
        )
    )
