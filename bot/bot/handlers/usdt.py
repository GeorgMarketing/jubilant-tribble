from aiogram import Router, F
from aiogram.types import CallbackQuery

from ..texts import USDT_INFO, CONTACT_REDIRECT
from ..keyboards import back_home_kb, usdt_kb, chat_link_kb
from ..config import settings
from ..db import set_user_funnel, log_event


router = Router()


def register_usdt(r: Router) -> None:
    r.callback_query.register(open_usdt, F.data == "usdt")
    r.callback_query.register(send_chat_link, F.data.startswith("chat_link:"))


async def open_usdt(query: CallbackQuery) -> None:
    await set_user_funnel(query.from_user.id, "usdt")
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "btn:usdt")
    await query.message.edit_text(USDT_INFO, reply_markup=usdt_kb())
    await query.answer()

    
@router.callback_query(F.data.startswith("chat_link:"))
async def send_chat_link(query: CallbackQuery) -> None:
    kind = query.data.split(":", 1)[1]
    link = settings.CHAT_LINK_DEFAULT
    if kind == "usdt":
        link = settings.CHAT_LINK_USDT or settings.CHAT_LINK_DEFAULT
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, f"chat_link:{kind}")
    await query.message.edit_text(f"{CONTACT_REDIRECT}\n\nСсылка: {link}", reply_markup=back_home_kb())
    await query.answer()


