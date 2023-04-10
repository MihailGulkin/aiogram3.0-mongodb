import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.infrastracture.adapters.db.main import create_mongo_client

from src.presentation.di.container import container
from src.presentation.di.providers.services import get_salary_usecase
from src.presentation.handlers import salary_router

from src.config import get_settings

logger = logging.getLogger(__name__)


async def main():
    config = get_settings()

    bot = Bot(token=config.BOT_TOKEN.get_secret_value())

    client = create_mongo_client(config.MONGO_DB_URL.get_secret_value())

    container.container.register(
        get_salary_usecase,
        instance=client
    )
    dp = Dispatcher()

    from src.presentation.middleware import (
        SalaryRepositoriesMiddleware
    )
    dp.update.middleware(
        SalaryRepositoriesMiddleware()
    )
    dp.include_router(salary_router)

    await bot.delete_webhook(drop_pending_updates=True)

    logger.warning('Start polling')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
