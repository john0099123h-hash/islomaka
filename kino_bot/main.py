"""
Kino Bot - Asosiy fayl
"""
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import load_config
from database import Database
from handlers import user_handlers, admin_handlers, callback_handlers

# Logging sozlash
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main():
    """Botni ishga tushirish"""
    logger.info("Bot ishga tushmoqda...")
    
    # Konfiguratsiyani yuklash
    config = load_config()
    
    # Bot va Dispatcher yaratish
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    # Database yaratish
    db = Database()
    await db.create_tables()
    
    # Routerlarni ro'yxatdan o'tkazish
    dp.include_router(user_handlers.router)
    dp.include_router(admin_handlers.router)
    dp.include_router(callback_handlers.router)
    
    # Middleware - har bir handlerga db va admin_ids ni yuborish
    @dp.message.middleware()
    @dp.callback_query.middleware()
    async def inject_dependencies(handler, event, data):
        data['db'] = db
        data['admin_ids'] = config.tg_bot.admin_ids
        return await handler(event, data)
    
    # Botni ishga tushirish
    try:
        logger.info("Bot muvaffaqiyatli ishga tushdi!")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot to'xtatildi")
