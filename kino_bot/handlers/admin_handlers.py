"""
Admin handlerlar
"""
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.reply import get_admin_keyboard, get_main_keyboard, get_cancel_keyboard
from database import Database

router = Router()


class AddMovieStates(StatesGroup):
    """Kino qo'shish holatlari"""
    waiting_for_video = State()
    waiting_for_title = State()
    waiting_for_title_uz = State()
    waiting_for_year = State()
    waiting_for_genre = State()
    waiting_for_rating = State()
    waiting_for_description = State()


class DeleteMovieStates(StatesGroup):
    """Kino o'chirish holatlari"""
    waiting_for_id = State()


def is_admin(user_id: int, admin_ids: list) -> bool:
    """Foydalanuvchi admin ekanligini tekshirish"""
    return user_id in admin_ids


@router.message(Command("admin"))
async def admin_panel(message: Message, admin_ids: list):
    """Admin panel"""
    if not is_admin(message.from_user.id, admin_ids):
        await message.answer("❌ Sizda admin huquqi yo'q!")
        return
    
    await message.answer(
        "🔐 <b>Admin Panel</b>\n\n"
        "Quyidagi amallarni bajarishingiz mumkin:",
        parse_mode="HTML",
        reply_markup=get_admin_keyboard()
    )


@router.message(F.text == "➕ Kino qo'shish")
async def add_movie_start(message: Message, state: FSMContext, admin_ids: list):
    """Kino qo'shishni boshlash"""
    if not is_admin(message.from_user.id, admin_ids):
        await message.answer("❌ Sizda admin huquqi yo'q!")
        return
    
    await state.set_state(AddMovieStates.waiting_for_video)
    await message.answer(
        "📹 <b>Kino faylini yuboring:</b>\n\n"
        "Video yoki file sifatida yuborishingiz mumkin.",
        parse_mode="HTML",
        reply_markup=get_cancel_keyboard()
    )


@router.message(AddMovieStates.waiting_for_video, F.video | F.document)
async def add_movie_video(message: Message, state: FSMContext):
    """Video qabul qilish"""
    file_id = message.video.file_id if message.video else message.document.file_id
    file_type = 'video' if message.video else 'document'
    
    await state.update_data(file_id=file_id, file_type=file_type)
    await state.set_state(AddMovieStates.waiting_for_title)
    
    await message.answer(
        "✍️ <b>Kino nomini kiriting (inglizcha):</b>\n\n"
        "Masalan: Avatar",
        parse_mode="HTML"
    )


@router.message(AddMovieStates.waiting_for_title)
async def add_movie_title(message: Message, state: FSMContext):
    """Nom qabul qilish"""
    await state.update_data(title=message.text)
    await state.set_state(AddMovieStates.waiting_for_title_uz)
    
    await message.answer(
        "✍️ <b>Kino nomini kiriting (o'zbekcha):</b>\n\n"
        "Masalan: Avatar yoki /skip"
    )


@router.message(AddMovieStates.waiting_for_title_uz)
async def add_movie_title_uz(message: Message, state: FSMContext):
    """O'zbek nomini qabul qilish"""
    title_uz = None if message.text == '/skip' else message.text
    await state.update_data(title_uz=title_uz)
    await state.set_state(AddMovieStates.waiting_for_year)
    
    await message.answer(
        "📅 <b>Kino yilini kiriting:</b>\n\n"
        "Masalan: 2009 yoki /skip"
    )


@router.message(AddMovieStates.waiting_for_year)
async def add_movie_year(message: Message, state: FSMContext):
    """Yilni qabul qilish"""
    year = None
    if message.text != '/skip':
        try:
            year = int(message.text)
        except ValueError:
            await message.answer("❌ Iltimos, to'g'ri yil kiriting!")
            return
    
    await state.update_data(year=year)
    await state.set_state(AddMovieStates.waiting_for_genre)
    
    await message.answer(
        "🎭 <b>Janrni kiriting:</b>\n\n"
        "Masalan: Action, Comedy yoki /skip"
    )


@router.message(AddMovieStates.waiting_for_genre)
async def add_movie_genre(message: Message, state: FSMContext):
    """Janrni qabul qilish"""
    genre = None if message.text == '/skip' else message.text
    await state.update_data(genre=genre)
    await state.set_state(AddMovieStates.waiting_for_rating)
    
    await message.answer(
        "⭐️ <b>Reytingni kiriting (0-10):</b>\n\n"
        "Masalan: 8.5 yoki /skip"
    )


@router.message(AddMovieStates.waiting_for_rating)
async def add_movie_rating(message: Message, state: FSMContext):
    """Reytingni qabul qilish"""
    rating = None
    if message.text != '/skip':
        try:
            rating = float(message.text)
            if not 0 <= rating <= 10:
                await message.answer("❌ Reyting 0 dan 10 gacha bo'lishi kerak!")
                return
        except ValueError:
            await message.answer("❌ Iltimos, to'g'ri reyting kiriting!")
            return
    
    await state.update_data(rating=rating)
    await state.set_state(AddMovieStates.waiting_for_description)
    
    await message.answer(
        "📝 <b>Kino haqida qisqacha ma'lumot:</b>\n\n"
        "Yoki /skip"
    )


@router.message(AddMovieStates.waiting_for_description)
async def add_movie_description(message: Message, state: FSMContext, db: Database):
    """Tavsifni qabul qilish va saqlash"""
    description = None if message.text == '/skip' else message.text
    
    # Barcha ma'lumotlarni olish
    data = await state.get_data()
    data['description'] = description
    data['added_by'] = message.from_user.id
    
    # Bazaga qo'shish
    try:
        movie_id = await db.add_movie(**data)
        
        await message.answer(
            f"✅ <b>Kino muvaffaqiyatli qo'shildi!</b>\n\n"
            f"🆔 ID: {movie_id}\n"
            f"🎬 Nom: {data['title']}\n"
            f"📅 Yil: {data['year'] or '-'}\n"
            f"🎭 Janr: {data['genre'] or '-'}\n"
            f"⭐️ Reyting: {data['rating'] or '-'}",
            parse_mode="HTML",
            reply_markup=get_admin_keyboard()
        )
    except Exception as e:
        await message.answer(
            f"❌ Xatolik yuz berdi: {str(e)}",
            reply_markup=get_admin_keyboard()
        )
    
    await state.clear()


@router.message(F.text == "🗑 Kino o'chirish")
async def delete_movie_start(message: Message, state: FSMContext, admin_ids: list):
    """Kino o'chirishni boshlash"""
    if not is_admin(message.from_user.id, admin_ids):
        await message.answer("❌ Sizda admin huquqi yo'q!")
        return
    
    await state.set_state(DeleteMovieStates.waiting_for_id)
    await message.answer(
        "🗑 <b>O'chirmoqchi bo'lgan kino ID raqamini kiriting:</b>",
        parse_mode="HTML",
        reply_markup=get_cancel_keyboard()
    )


@router.message(DeleteMovieStates.waiting_for_id)
async def delete_movie_confirm(message: Message, state: FSMContext, db: Database):
    """Kino o'chirishni tasdiqlash"""
    try:
        movie_id = int(message.text)
    except ValueError:
        await message.answer("❌ Iltimos, to'g'ri ID raqam kiriting!")
        return
    
    movie = await db.get_movie_by_id(movie_id)
    if not movie:
        await message.answer("❌ Bunday ID bilan kino topilmadi!")
        return
    
    await db.delete_movie(movie_id)
    await message.answer(
        f"✅ <b>Kino o'chirildi:</b>\n\n"
        f"🎬 {movie['title']}",
        parse_mode="HTML",
        reply_markup=get_admin_keyboard()
    )
    
    await state.clear()


@router.message(F.text == "📊 Statistika")
async def admin_stats(message: Message, db: Database, admin_ids: list):
    """Admin statistikasi"""
    if not is_admin(message.from_user.id, admin_ids):
        await message.answer("❌ Sizda admin huquqi yo'q!")
        return
    
    stats = await db.get_stats()
    
    stats_text = (
        "📊 <b>Bot Statistikasi:</b>\n\n"
        f"🎬 Jami kinolar: {stats['total_movies']}\n"
        f"👥 Foydalanuvchilar: {stats['total_users']}\n"
        f"🔍 Qidiruvlar soni: {stats['total_searches']}\n"
    )
    
    await message.answer(stats_text, parse_mode="HTML")


@router.message(F.text == "🔙 Orqaga")
async def back_to_main(message: Message):
    """Asosiy menyuga qaytish"""
    await message.answer(
        "📱 Asosiy menyu:",
        reply_markup=get_main_keyboard()
    )


@router.message(F.text == "❌ Bekor qilish")
async def cancel_action(message: Message, state: FSMContext):
    """Amalni bekor qilish"""
    await state.clear()
    await message.answer(
        "❌ Amal bekor qilindi",
        reply_markup=get_main_keyboard()
    )
