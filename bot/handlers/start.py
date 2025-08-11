from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from ..texts import WELCOME_TITLE, HELLO
from ..keyboards import main_menu_kb
from ..db import init_db, upsert_user, log_event


router = Router()


def register_start(r: Router) -> None:
    r.message.register(cmd_start, CommandStart())
    r.callback_query.register(on_back_home, F.data == "back_home")


async def cmd_start(message: Message) -> None:
    await init_db()
    await upsert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        full_name=message.from_user.full_name,
    )
    await log_event(message.from_user.id, message.from_user.username, message.from_user.full_name, "cmd:/start")
    await message.answer(WELCOME_TITLE)
    await message.answer(HELLO, reply_markup=main_menu_kb())


async def on_back_home(query: CallbackQuery) -> None:
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "btn:back_home")
    await query.message.edit_text(HELLO, reply_markup=main_menu_kb())
    await query.answer()


