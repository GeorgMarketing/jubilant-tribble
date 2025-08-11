from aiogram import Router, F
from aiogram.types import CallbackQuery

from ..texts import (
    FAQ_Q_AGENT,
    FAQ_A_AGENT,
    FAQ_Q_SANCTIONS,
    FAQ_A_SANCTIONS,
    FAQ_Q_GUARANTEES,
    FAQ_A_GUARANTEES,
    FAQ_Q_DOCS,
    FAQ_A_DOCS,
)
from ..keyboards import faq_kb
from ..db import log_event


router = Router()


def register_faq(r: Router) -> None:
    r.callback_query.register(show_agent, F.data == "faq_agent")
    r.callback_query.register(show_sanctions, F.data == "faq_sanctions")
    r.callback_query.register(show_guarantees, F.data == "faq_guarantees")
    r.callback_query.register(show_docs, F.data == "faq_docs")


async def show_agent(query: CallbackQuery) -> None:
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "faq:agent")
    await query.message.edit_text(f"{FAQ_Q_AGENT}\n\n{FAQ_A_AGENT}", reply_markup=faq_kb())
    await query.answer()


async def show_sanctions(query: CallbackQuery) -> None:
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "faq:sanctions")
    await query.message.edit_text(f"{FAQ_Q_SANCTIONS}\n\n{FAQ_A_SANCTIONS}", reply_markup=faq_kb())
    await query.answer()


async def show_guarantees(query: CallbackQuery) -> None:
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "faq:guarantees")
    await query.message.edit_text(f"{FAQ_Q_GUARANTEES}\n\n{FAQ_A_GUARANTEES}", reply_markup=faq_kb())
    await query.answer()


async def show_docs(query: CallbackQuery) -> None:
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "faq:docs")
    await query.message.edit_text(f"{FAQ_Q_DOCS}\n\n{FAQ_A_DOCS}", reply_markup=faq_kb())
    await query.answer()


