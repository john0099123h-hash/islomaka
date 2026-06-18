"""
Callback query handlerlar
"""
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from keyboards.inline import get_movie_keyboard, get_movies_pagination, get_confirmation_keyboard
from database import Database

router = Router()


@router.callback_query(F.data.startswith("movie_"))
async def show_movie_details(callback: CallbackQuery, db: Database, admin_ids: list):
    """Kino tafsilotlarini ko'rsatish"""
    movie_id = int(callback.data.split("_")[1])
    movie = await db.get_movie_by_id(movie_id)
    
    if not movie:
        await callback.answer("❌ Kino topilmadi!", show_alert=True)
        return
    
    # Kino haqida ma'lumot
    title = movie.get('title_uz') or movie.get('title')
    year = f"\n📅 Yil: {movie['year']}" if movie.get('year') else ""
    genre = f"\n🎭 Janr: {movie['genre']}" if movie.get('genre') else ""
    rating = f"\n⭐️ Reyting: {movie['rating']}/10" if movie.get('rating') else ""
    description = f"\n\n📝 {movie['description']}" if movie.get('description') else ""
    
    info_text = (
        f"🎬 <b>{title}</b>"
        f"{year}"
        f"{genre}"
        f"{rating}"
        f"{description}"
    )
    
    is_admin = callback.from_user.id in admin_ids
    
    await callback.message.answer(
        info_text,
        parse_mode="HTML",
        reply_markup=get_movie_keyboard(movie_id, is_admin)
    )
    await callback.answer()


@router.callback_query(F.data.startswith("download_"))
async def download_movie(callback: CallbackQuery, db: Database):
    """Kinoni yuborish"""
    movie_id = int(callback.data.split("_")[1])
    movie = await db.get_movie_by_id(movie_id)
    
    if not movie:
        await callback.answer("❌ Kino topilmadi!", show_alert=True)
        return
    
    await callback.answer("📥 Kino yuklanmoqda...")
    
    try:
        # Video yoki document sifatida yuborish
        if movie['file_type'] == 'video':
            await callback.message.answer_video(
                video=movie['file_id'],
                caption=f"🎬 {movie.get('title_uz') or movie.get('title')}"
            )
        else:
            await callback.message.answer_document(
                document=movie['file_id'],
                caption=f"🎬 {movie.get('title_uz') or movie.get('title')}"
            )
    except Exception as e:
        await callback.message.answer(
            f"❌ Xatolik: {str(e)}\n\n"
            "Fayl topilmadi yoki o'chirilgan."
        )


@router.callback_query(F.data.startswith("genre_"))
async def show_genre_movies(callback: CallbackQuery, db: Database):
    """Janr bo'yicha kinolarni ko'rsatish"""
    genre_map = {
        'action': 'Action',
        'comedy': 'Comedy',
        'drama': 'Drama',
        'horror': 'Horror',
        'scifi': 'Sci-Fi',
        'romance': 'Romance',
        'thriller': 'Thriller',
        'adventure': 'Adventure',
        'family': 'Family',
        'animation': 'Animation'
    }
    
    genre_key = callback.data.split("_")[1]
    genre = genre_map.get(genre_key, genre_key)
    
    movies = await db.get_movies_by_genre(genre)
    
    if not movies:
        await callback.answer(
            f"😔 {genre} janrida kinolar topilmadi!",
            show_alert=True
        )
        return
    
    await callback.message.edit_text(
        f"🎭 <b>{genre} janridagi kinolar ({len(movies)} ta):</b>",
        parse_mode="HTML",
        reply_markup=get_movies_pagination(movies)
    )
    await callback.answer()


@router.callback_query(F.data.startswith("page_"))
async def paginate_movies(callback: CallbackQuery):
    """Sahifalash"""
    page = int(callback.data.split("_")[1])
    
    # Bu yerda movies ro'yxatini qayta olish kerak
    # Hozircha faqat sahifa raqamini ko'rsatamiz
    await callback.answer(f"📄 Sahifa {page + 1}")


@router.callback_query(F.data.startswith("delete_"))
async def confirm_delete(callback: CallbackQuery, admin_ids: list):
    """O'chirishni tasdiqlash"""
    if callback.from_user.id not in admin_ids:
        await callback.answer("❌ Sizda admin huquqi yo'q!", show_alert=True)
        return
    
    movie_id = int(callback.data.split("_")[1])
    
    await callback.message.edit_text(
        "⚠️ <b>Kinoni o'chirishni tasdiqlaysizmi?</b>\n\n"
        "Bu amal qaytarib bo'lmaydi!",
        parse_mode="HTML",
        reply_markup=get_confirmation_keyboard("delete", movie_id)
    )
    await callback.answer()


@router.callback_query(F.data.startswith("confirm_delete_"))
async def delete_movie_confirmed(callback: CallbackQuery, db: Database, admin_ids: list):
    """O'chirishni amalga oshirish"""
    if callback.from_user.id not in admin_ids:
        await callback.answer("❌ Sizda admin huquqi yo'q!", show_alert=True)
        return
    
    movie_id = int(callback.data.split("_")[2])
    movie = await db.get_movie_by_id(movie_id)
    
    if not movie:
        await callback.answer("❌ Kino topilmadi!", show_alert=True)
        return
    
    await db.delete_movie(movie_id)
    
    await callback.message.edit_text(
        f"✅ <b>Kino o'chirildi:</b>\n\n"
        f"🎬 {movie.get('title_uz') or movie.get('title')}",
        parse_mode="HTML"
    )
    await callback.answer("✅ Kino o'chirildi!")


@router.callback_query(F.data.startswith("cancel_"))
async def cancel_action(callback: CallbackQuery):
    """Amalni bekor qilish"""
    await callback.message.edit_text("❌ Amal bekor qilindi")
    await callback.answer()
