import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.webhook.aiohttp_server import (
    SimpleRequestHandler,
    setup_application,
)
from aiohttp import web

from .config import settings
from .handlers import (
    register_start,
    register_navigation,
    register_faq,
    register_roles,
    register_usdt,
)


async def main() -> None:
    logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))

    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    # register routers
    register_start(dp)
    register_navigation(dp)
    register_faq(dp)
    register_roles(dp)
    register_usdt(dp)
    if settings.WEBHOOK_URL:
        # webhook mode
        app = web.Application()
        SimpleRequestHandler(
            dispatcher=dp,
            bot=bot,
            secret_token=settings.WEBHOOK_SECRET,
        ).register(app, path=settings.WEBHOOK_PATH)

        setup_application(app, dp, bot=bot)

        await bot.set_webhook(
            url=settings.WEBHOOK_URL.rstrip("/") + settings.WEBHOOK_PATH,
            secret_token=settings.WEBHOOK_SECRET,
            drop_pending_updates=True,
        )
        logging.info("Webhook set to %s", settings.WEBHOOK_URL)
        await web._run_app(app, host=settings.WEBAPP_HOST, port=settings.WEBAPP_PORT)
    else:
        # polling mode
        try:
            await bot.delete_webhook(drop_pending_updates=True)
        except Exception:
            pass
        await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass


