import json

from pydantic import ValidationError

from aiogram import types, F, Router
from aiogram.filters.command import Command

from src.domain.const.error import ERROR_MESSAGE
from src.domain.dto.query import AggregateQuery

from src.domain.interfaces.usecase import BaseSalaryUseCase

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.username}")


@router.message(F.text)
async def aggregate_salary(
        message: types.Message,
        salary_usecase: BaseSalaryUseCase
) -> None:
    try:
        json_object = json.loads(message.text)

        salary = await salary_usecase(
            AggregateQuery(**json_object)
        )
        await message.answer(str(salary.dict()))
    except TypeError:
        await message.answer(ERROR_MESSAGE)
    except json.decoder.JSONDecodeError:
        await message.answer(ERROR_MESSAGE)
    except ValidationError:
        await message.answer(ERROR_MESSAGE)
