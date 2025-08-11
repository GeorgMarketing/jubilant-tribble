from aiogram import Router, F
from aiogram.types import CallbackQuery

from ..texts import ROLE_CHOOSE, FAQ_INTRO
from ..keyboards import role_kb, faq_kb
from ..db import set_user_funnel, log_event


router = Router()


def register_navigation(r: Router) -> None:
    r.callback_query.register(open_roles, F.data == "role")
    r.callback_query.register(open_faq, F.data == "faq")


async def open_roles(query: CallbackQuery) -> None:
    await set_user_funnel(query.from_user.id, "role")
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "btn:role")
    await query.message.edit_text(ROLE_CHOOSE, reply_markup=role_kb())
    await query.answer()


async def open_faq(query: CallbackQuery) -> None:
    await set_user_funnel(query.from_user.id, "faq")
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "btn:faq")
    await query.message.edit_text(FAQ_INTRO, reply_markup=faq_kb())
    await query.answer()


