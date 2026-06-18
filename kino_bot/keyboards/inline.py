"""
Inline klaviaturalar
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import List, Dict


def get_movie_keyboard(movie_id: int, is_admin: bool = False) -> InlineKeyboardMarkup:
    """Kino uchun klaviatura"""
    buttons = []
    
    # Yuklash tugmasi
    buttons.append([InlineKeyboardButton(text="📥 Yuklash", callback_data=f"download_{movie_id}")])
    
    # Admin uchun o'chirish tugmasi
    if is_admin:
        buttons.append([InlineKeyboardButton(text="🗑 O'chirish", callback_data=f"delete_{movie_id}")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_genre_keyboard() -> InlineKeyboardMarkup:
    """Janrlar klaviaturasi"""
    genres = [
        ("🎬 Aksiya", "genre_action"),
        ("😂 Komediya", "genre_comedy"),
        ("💔 Drama", "genre_drama"),
        ("😱 Qo'rqinchli", "genre_horror"),
        ("🔬 Fantastika", "genre_scifi"),
        ("❤️ Romantika", "genre_romance"),
        ("🕵️ Thriller", "genre_thriller"),
        ("🏃 Sarguzasht", "genre_adventure"),
        ("👨‍👩‍👧 Oilaviy", "genre_family"),
        ("📽 Animatsiya", "genre_animation")
    ]
    
    buttons = []
    row = []
    for i, (text, callback) in enumerate(genres):
        row.append(InlineKeyboardButton(text=text, callback_data=callback))
        if len(row) == 2 or i == len(genres) - 1:
            buttons.append(row)
            row = []
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_movies_pagination(movies: List[Dict], page: int = 0, per_page: int = 5) -> InlineKeyboardMarkup:
    """Kinolar ro'yxati uchun sahifalash"""
    buttons = []
    
    start = page * per_page
    end = start + per_page
    page_movies = movies[start:end]
    
    for movie in page_movies:
        title = movie.get('title_uz') or movie.get('title')
        year = f" ({movie['year']})" if movie.get('year') else ""
        buttons.append([
            InlineKeyboardButton(
                text=f"{title}{year}",
                callback_data=f"movie_{movie['id']}"
            )
        ])
    
    # Sahifalash tugmalari
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"page_{page-1}"))
    if end < len(movies):
        nav_buttons.append(InlineKeyboardButton(text="➡️ Keyingi", callback_data=f"page_{page+1}"))
    
    if nav_buttons:
        buttons.append(nav_buttons)
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_confirmation_keyboard(action: str, item_id: int) -> InlineKeyboardMarkup:
    """Tasdiqlash klaviaturasi"""
    buttons = [
        [
            InlineKeyboardButton(text="✅ Ha", callback_data=f"confirm_{action}_{item_id}"),
            InlineKeyboardButton(text="❌ Yo'q", callback_data=f"cancel_{action}")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
