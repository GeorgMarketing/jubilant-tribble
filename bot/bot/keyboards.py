from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Выбрать деятельность", callback_data="role")],
            [InlineKeyboardButton(text="Частые вопросы (FAQ)", callback_data="faq")],
            [InlineKeyboardButton(text="Покупка USDT", callback_data="usdt")],
            [InlineKeyboardButton(text="Связь с менеджером", callback_data="manager")],
        ]
    )


def role_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Бизнес", callback_data="role_business")],
            [InlineKeyboardButton(text="Физ лицо", callback_data="role_individual")],
            [InlineKeyboardButton(text="Нерезидент", callback_data="role_nonresident")],
            [InlineKeyboardButton(text="В главное меню", callback_data="back_home")],
        ]
    )


def business_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Импорт/Экспорт", callback_data="biz_import_export")],
            [InlineKeyboardButton(text="Селлеры маркетплейсов", callback_data="biz_marketplace")],
            [InlineKeyboardButton(text="В главное меню", callback_data="back_home")],
        ]
    )


def yes_no_kb(prefix: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Да", callback_data=f"{prefix}:yes")],
            [InlineKeyboardButton(text="Нет", callback_data=f"{prefix}:no")],
            [InlineKeyboardButton(text="В главное меню", callback_data="back_home")],
        ]
    )


def core_steps_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Получить персональную ссылку на регистрацию", callback_data="core_link")],
            [InlineKeyboardButton(text="Что такое CORE?", callback_data="core_about")],
            [InlineKeyboardButton(text="Остались вопросы (к менеджеру)", callback_data="manager")],
            [InlineKeyboardButton(text="В главное меню", callback_data="back_home")],
        ]
    )


def faq_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Платежный агент — кто он?", callback_data="faq_agent")],
            [InlineKeyboardButton(text="Как вы действуете во время санкций?", callback_data="faq_sanctions")],
            [InlineKeyboardButton(text="Какие гарантии предоставляете?", callback_data="faq_guarantees")],
            [InlineKeyboardButton(text="Какие документы нужны?", callback_data="faq_docs")],
            [InlineKeyboardButton(text="В главное меню", callback_data="back_home")],
        ]
    )


def back_home_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="В главное меню", callback_data="back_home")]]
    )


def individual_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Связь с менеджером", callback_data="manager")],
            [InlineKeyboardButton(text="В главное меню", callback_data="back_home")],
        ]
    )


def core_about_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Получить ссылку", callback_data="core_link")],
            [InlineKeyboardButton(text="Остались вопросы (к менеджеру)", callback_data="manager")],
            [InlineKeyboardButton(text="Главное меню", callback_data="back_home")],
        ]
    )


def chat_link_kb(kind: str = "default") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ссылка на чат", callback_data=f"chat_link:{kind}")],
            [InlineKeyboardButton(text="В главное меню", callback_data="back_home")],
        ]
    )


def usdt_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Начать чат по покупке/оплате USDT", callback_data="chat_link:usdt")],
            [InlineKeyboardButton(text="В главное меню", callback_data="back_home")],
        ]
    )


