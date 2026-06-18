"""
Database modellari va funksiyalari
"""
import aiosqlite
from typing import Optional, List, Dict
import logging

logger = logging.getLogger(__name__)


class Database:
    """Kinolar bazasi bilan ishlash"""
    
    def __init__(self, db_path: str = "kino_bot.db"):
        self.db_path = db_path
    
    async def create_tables(self):
        """Ma'lumotlar bazasi jadvallarini yaratish"""
        async with aiosqlite.connect(self.db_path) as db:
            # Kinolar jadvali
            await db.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    title_uz TEXT,
                    year INTEGER,
                    genre TEXT,
                    rating REAL,
                    description TEXT,
                    file_id TEXT,
                    file_type TEXT DEFAULT 'video',
                    added_by INTEGER,
                    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Foydalanuvchilar jadvali
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    is_admin BOOLEAN DEFAULT 0,
                    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_activity TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Qidiruv tarixi
            await db.execute("""
                CREATE TABLE IF NOT EXISTS search_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    query TEXT,
                    search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                )
            """)
            
            await db.commit()
            logger.info("Database tables created successfully")
    
    async def add_movie(self, title: str, file_id: str, **kwargs) -> int:
        """Yangi kino qo'shish"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("""
                INSERT INTO movies (title, title_uz, year, genre, rating, description, file_id, file_type, added_by)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                title,
                kwargs.get('title_uz'),
                kwargs.get('year'),
                kwargs.get('genre'),
                kwargs.get('rating'),
                kwargs.get('description'),
                file_id,
                kwargs.get('file_type', 'video'),
                kwargs.get('added_by')
            ))
            await db.commit()
            return cursor.lastrowid
    
    async def search_movies(self, query: str, limit: int = 10) -> List[Dict]:
        """Kino qidirish"""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("""
                SELECT * FROM movies 
                WHERE title LIKE ? OR title_uz LIKE ? OR description LIKE ?
                ORDER BY rating DESC, year DESC
                LIMIT ?
            """, (f'%{query}%', f'%{query}%', f'%{query}%', limit))
            
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
    
    async def get_movie_by_id(self, movie_id: int) -> Optional[Dict]:
        """ID bo'yicha kinoni olish"""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
            row = await cursor.fetchone()
            return dict(row) if row else None
    
    async def get_all_movies(self, limit: int = 50, offset: int = 0) -> List[Dict]:
        """Barcha kinolarni olish"""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("""
                SELECT * FROM movies 
                ORDER BY added_date DESC 
                LIMIT ? OFFSET ?
            """, (limit, offset))
            
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
    
    async def delete_movie(self, movie_id: int) -> bool:
        """Kinoni o'chirish"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
            await db.commit()
            return True
    
    async def add_user(self, user_id: int, username: str = None, 
                      first_name: str = None, last_name: str = None, 
                      is_admin: bool = False):
        """Foydalanuvchi qo'shish yoki yangilash"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO users (user_id, username, first_name, last_name, is_admin)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    username = excluded.username,
                    first_name = excluded.first_name,
                    last_name = excluded.last_name,
                    last_activity = CURRENT_TIMESTAMP
            """, (user_id, username, first_name, last_name, is_admin))
            await db.commit()
    
    async def add_search_history(self, user_id: int, query: str):
        """Qidiruv tarixiga qo'shish"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO search_history (user_id, query)
                VALUES (?, ?)
            """, (user_id, query))
            await db.commit()
    
    async def get_movies_by_genre(self, genre: str, limit: int = 20) -> List[Dict]:
        """Janr bo'yicha kinolarni olish"""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("""
                SELECT * FROM movies 
                WHERE genre LIKE ?
                ORDER BY rating DESC, year DESC
                LIMIT ?
            """, (f'%{genre}%', limit))
            
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
    
    async def get_stats(self) -> Dict:
        """Statistika olish"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("SELECT COUNT(*) as total_movies FROM movies")
            movies_count = (await cursor.fetchone())[0]
            
            cursor = await db.execute("SELECT COUNT(*) as total_users FROM users")
            users_count = (await cursor.fetchone())[0]
            
            cursor = await db.execute("SELECT COUNT(*) as total_searches FROM search_history")
            searches_count = (await cursor.fetchone())[0]
            
            return {
                'total_movies': movies_count,
                'total_users': users_count,
                'total_searches': searches_count
            }
