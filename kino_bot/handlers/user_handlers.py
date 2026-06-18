"""
Foydalanuvchilar uchun handlerlar
"""
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.reply import get_main_keyboard
from keyboards.inline import get_genre_keyboard, get_movies_pagination
from database import Database

router = Router()


class SearchStates(StatesGroup):
    """Qidiruv holatlari"""
    waiting_for_query = State()


@router.message(CommandStart())
async def cmd_start(message: Message, db: Database):
    """Start komandasi"""
    user = message.from_user
    
    # Foydalanuvchini bazaga qo'shish
    await db.add_user(
        user_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name
    )
    
    welcome_text = (
        f"👋 Assalomu alaykum, {user.first_name}!\n\n"
        "🎬 Kino Bot'ga xush kelibsiz!\n\n"
        "Bu bot orqali siz:\n"
        "🔍 Kinolarni qidirishingiz\n"
        "📥 Kinolarni yuklab olishingiz\n"
        "🎭 Janr bo'yicha tanlashingiz mumkin\n\n"
        "Quyidagi tugmalardan birini tanlang 👇"
    )
    
    await message.answer(welcome_text, reply_markup=get_main_keyboard())


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Yordam komandasi"""
    help_text = (
        "📖 <b>Bot qo'llanmasi:</b>\n\n"
        "🔍 <b>Kino qidirish</b> - Kino nomini yozing va qidiring\n"
        "📋 <b>Barcha kinolar</b> - Bazadagi barcha kinolarni ko'ring\n"
        "🎭 <b>Janrlar</b> - Janr bo'yicha kinolarni toping\n"
        "ℹ️ <b>Bot haqida</b> - Bot haqida ma'lumot\n\n"
        "<b>Komandalar:</b>\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam\n"
        "/search - Kino qidirish\n"
        "/genres - Janrlar ro'yxati\n"
    )
    
    await message.answer(help_text, parse_mode="HTML")


@router.message(F.text == "🔍 Kino qidirish")
@router.message(Command("search"))
async def search_start(message: Message, state: FSMContext):
    """Qidiruv boshlanishi"""
    await state.set_state(SearchStates.waiting_for_query)
    await message.answer(
        "🔍 Qidirayotgan kinongiz nomini yozing:\n\n"
        "Masalan: Avatar, Titanik, Spider-Man",
        reply_markup=get_main_keyboard()
    )


@router.message(SearchStates.waiting_for_query)
async def search_process(message: Message, state: FSMContext, db: Database):
    """Qidiruvni amalga oshirish"""
    query = message.text.strip()
    
    if not query:
        await message.answer("❌ Iltimos, kino nomini kiriting!")
        return
    
    # Qidiruv tarixiga qo'shish
    await db.add_search_history(message.from_user.id, query)
    
    # Kinolarni qidirish
    movies = await db.search_movies(query)
    
    if not movies:
        await message.answer(
            f"😔 '{query}' nomi bo'yicha kinolar topilmadi.\n\n"
            "Boshqa nom bilan qayta urinib ko'ring yoki /start tugmasini bosing."
        )
    else:
        await message.answer(
            f"✅ <b>{len(movies)} ta kino topildi:</b>\n\n"
            f"Qidiruv natijasi: <i>{query}</i>",
            parse_mode="HTML",
            reply_markup=get_movies_pagination(movies)
        )
    
    await state.clear()


@router.message(F.text == "📋 Barcha kinolar")
async def show_all_movies(message: Message, db: Database):
    """Barcha kinolarni ko'rsatish"""
    movies = await db.get_all_movies(limit=20)
    
    if not movies:
        await message.answer(
            "😔 Hozircha bazada kinolar yo'q.\n\n"
            "Tez orada yangi kinolar qo'shiladi!"
        )
        return
    
    await message.answer(
        f"📋 <b>Bazadagi kinolar ({len(movies)} ta):</b>",
        parse_mode="HTML",
        reply_markup=get_movies_pagination(movies)
    )


@router.message(F.text == "🎭 Janrlar")
@router.message(Command("genres"))
async def show_genres(message: Message):
    """Janrlarni ko'rsatish"""
    await message.answer(
        "🎭 <b>Janrni tanlang:</b>",
        parse_mode="HTML",
        reply_markup=get_genre_keyboard()
    )


@router.message(F.text == "ℹ️ Bot haqida")
async def about_bot(message: Message, db: Database):
    """Bot haqida ma'lumot"""
    stats = await db.get_stats()
    
    about_text = (
        "ℹ️ <b>Kino Bot haqida</b>\n\n"
        "🎬 Versiya: 1.0.0\n"
        f"📊 Bazada kinolar: {stats['total_movies']} ta\n"
        f"👥 Foydalanuvchilar: {stats['total_users']} ta\n"
        f"🔍 Qidiruvlar: {stats['total_searches']} ta\n\n"
        "💡 Bu bot sizga eng yaxshi kinolarni topishda yordam beradi!\n\n"
        "📬 Murojaat: @your_admin"
    )
    
    await message.answer(about_text, parse_mode="HTML")


@router.message(Command("stats"))
async def show_stats(message: Message, db: Database):
    """Statistika"""
    stats = await db.get_stats()
    
    stats_text = (
        "📊 <b>Statistika:</b>\n\n"
        f"🎬 Jami kinolar: {stats['total_movies']}\n"
        f"👥 Foydalanuvchilar: {stats['total_users']}\n"
        f"🔍 Qidiruvlar: {stats['total_searches']}\n"
    )
    
    await message.answer(stats_text, parse_mode="HTML")
