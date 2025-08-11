from aiogram import Router, F
from aiogram.types import CallbackQuery

from ..texts import (
    ROLE_INDIVIDUAL_TEXT,
    ROLE_BUSINESS_ASK,
    ROLE_NONRESIDENT_ASK_INVOICE,
    STEPS_CORE,
    CORE_ABOUT,
    CONTACT_REDIRECT,
)
from ..keyboards import business_kb, yes_no_kb, core_steps_kb, back_home_kb, core_about_kb, individual_kb
from ..config import settings
from ..db import set_user_role, set_user_funnel, log_event


router = Router()


def register_roles(r: Router) -> None:
    r.callback_query.register(role_business, F.data == "role_business")
    r.callback_query.register(role_individual, F.data == "role_individual")
    r.callback_query.register(role_nonresident, F.data == "role_nonresident")

    # бизнес подветки
    r.callback_query.register(biz_import_export, F.data == "biz_import_export")
    r.callback_query.register(biz_marketplace, F.data == "biz_marketplace")
    r.callback_query.register(biz_contract_answer, F.data.startswith("biz_contract:"))

    # нерезидент
    r.callback_query.register(nonresident_invoice_answer, F.data.startswith("nonresident_invoice:"))

    # общие
    r.callback_query.register(core_link, F.data == "core_link")
    r.callback_query.register(to_manager, F.data == "manager")
    r.callback_query.register(core_about, F.data == "core_about")


async def role_business(query: CallbackQuery) -> None:
    await set_user_role(query.from_user.id, "business")
    await set_user_funnel(query.from_user.id, "business")
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "role:business")
    await query.message.edit_text("Выберите направление бизнеса:", reply_markup=business_kb())
    await query.answer()


async def role_individual(query: CallbackQuery) -> None:
    await set_user_role(query.from_user.id, "individual")
    await set_user_funnel(query.from_user.id, "usdt")
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "role:individual")
    await query.message.edit_text(ROLE_INDIVIDUAL_TEXT, reply_markup=individual_kb())
    await query.answer()


async def role_nonresident(query: CallbackQuery) -> None:
    await set_user_role(query.from_user.id, "nonresident")
    await set_user_funnel(query.from_user.id, "nonresident")
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "role:nonresident")
    await query.message.edit_text(ROLE_NONRESIDENT_ASK_INVOICE, reply_markup=yes_no_kb("nonresident_invoice"))
    await query.answer()


async def biz_import_export(query: CallbackQuery) -> None:
    await set_user_funnel(query.from_user.id, "import_export")
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "biz:import_export")
    await query.message.edit_text(ROLE_BUSINESS_ASK, reply_markup=yes_no_kb("biz_contract"))
    await query.answer()


async def biz_marketplace(query: CallbackQuery) -> None:
    await set_user_funnel(query.from_user.id, "marketplace")
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "biz:marketplace")
    await query.message.edit_text(ROLE_BUSINESS_ASK, reply_markup=yes_no_kb("biz_contract"))
    await query.answer()


async def biz_contract_answer(query: CallbackQuery) -> None:
    answer = query.data.split(":", 1)[1]
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, f"biz_contract:{answer}")
    if answer == "yes":
        await query.message.edit_text(STEPS_CORE, reply_markup=core_steps_kb())
    else:
        await query.message.edit_text(f"{CONTACT_REDIRECT}\n\nСсылка: {settings.CHAT_LINK_DEFAULT}", reply_markup=back_home_kb())
    await query.answer()


async def nonresident_invoice_answer(query: CallbackQuery) -> None:
    answer = query.data.split(":", 1)[1]
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, f"nonresident_invoice:{answer}")
    if answer == "yes":
        await query.message.edit_text(STEPS_CORE, reply_markup=core_steps_kb())
    else:
        await query.message.edit_text(f"{CONTACT_REDIRECT}\n\nСсылка: {settings.CHAT_LINK_DEFAULT}", reply_markup=back_home_kb())
    await query.answer()


async def core_link(query: CallbackQuery) -> None:
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "core:link")
    await query.message.edit_text(f"Персональная ссылка на регистрацию: {settings.CORE_REG_URL}", reply_markup=back_home_kb())
    await query.answer()


async def to_manager(query: CallbackQuery) -> None:
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "contact:manager")
    await query.message.edit_text(f"Связаться с менеджером: {settings.MANAGER_URL}", reply_markup=back_home_kb())
    await query.answer()


async def core_about(query: CallbackQuery) -> None:
    await log_event(query.from_user.id, query.from_user.username, query.from_user.full_name, "core:about")
    await query.message.edit_text(CORE_ABOUT, reply_markup=core_about_kb())
    await query.answer()


