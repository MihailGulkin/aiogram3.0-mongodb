import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.infrastracture.db.main import create_mongo_client
from src.infrastracture.db.middleware import SalaryRepositoriesMiddleware

from src.presentation.handlers import salary_router
from src.config import get_settings

logger = logging.getLogger(__name__)


async def main():
    config = get_settings()

    client = create_mongo_client(config.MONGO_DB_URL.get_secret_value())

    bot = Bot(token=config.BOT_TOKEN.get_secret_value())

    dp = Dispatcher()

    dp.update.middleware(SalaryRepositoriesMiddleware(client=client))
    dp.include_router(salary_router)

    await bot.delete_webhook(drop_pending_updates=True)

    logger.warning('Start polling')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
