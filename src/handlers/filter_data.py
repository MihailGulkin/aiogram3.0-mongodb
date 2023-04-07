import json

from aiogram import types, F, Router
from aiogram.filters.command import Command

from pydantic import ValidationError

from src.schemas import AggregateQuery

router = Router()

msg_const = """
Невалидный запос. Пример запроса:
{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}"""


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.username}")


@router.message(F.text)
async def get_json_db_filter(message: types.Message):
    try:
        json_object = json.loads(message.text)
        obj = AggregateQuery(**json_object)
    except TypeError:
        await message.answer(msg_const)
    except json.decoder.JSONDecodeError:
        await message.answer(msg_const)
    except ValidationError:
        await message.answer(msg_const)
