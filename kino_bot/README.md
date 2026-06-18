# 🎬 Kino Bot

Professional Telegram bot kinolarni qidirish, yuklash va boshqarish uchun.

## ⚡️ Xususiyatlar

- 🔍 **Kino qidirish** - Nom bo'yicha tezkor qidiruv
- 📋 **Kinolar bazasi** - Barcha kinolarni ko'rish
- 🎭 **Janrlar** - Janr bo'yicha filterlash
- 📥 **Yuklash** - Kinolarni to'g'ridan-to'g'ri Telegram orqali yuklash
- 👨‍💼 **Admin panel** - Kino qo'shish, o'chirish va statistika
- 📊 **Statistika** - Foydalanuvchilar va qidiruvlar statistikasi
- 🗄 **Database** - SQLite ma'lumotlar bazasi

## 📋 Talablar

- Python 3.8+
- Telegram Bot Token (@BotFather dan)

## 🚀 O'rnatish

### 1. Loyihani klonlash

```bash
git clone https://github.com/john0099123h-hash/islomaka.git
cd islomaka/kino_bot
```

### 2. Virtual muhit yaratish

```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Kerakli kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Konfiguratsiya

`.env.example` faylidan `.env` yarating va kerakli ma'lumotlarni kiriting:

```bash
cp .env.example .env
```

`.env` faylini tahrirlang:

```env
# Telegram Bot Token (@BotFather dan olingan)
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# Admin foydalanuvchilar ID raqamlari (vergul bilan ajrating)
ADMIN_IDS=123456789,987654321
```

**Bot Token olish:**
1. Telegram'da [@BotFather](https://t.me/BotFather) botini oching
2. `/newbot` buyrug'ini yuboring
3. Bot nomini kiriting
4. Username kiriting (masalan: my_kino_bot)
5. Token'ni nusxalang va `.env` fayliga qo'ying

**User ID ni olish:**
1. Telegram'da [@userinfobot](https://t.me/userinfobot) botini oching
2. `/start` bosing
3. ID raqamingizni nusxalang

### 5. Botni ishga tushirish

```bash
python main.py
```

Agar hamma narsa to'g'ri sozlangan bo'lsa, quyidagi xabar ko'rinadi:
```
INFO - Bot ishga tushmoqda...
INFO - Database tables created successfully
INFO - Bot muvaffaqiyatli ishga tushdi!
```

## 📱 Foydalanish

### Oddiy foydalanuvchilar uchun:

- `/start` - Botni ishga tushirish
- `/help` - Yordam
- `/search` - Kino qidirish
- `/genres` - Janrlar ro'yxati
- `🔍 Kino qidirish` - Qidiruv rejimini ochish
- `📋 Barcha kinolar` - Barcha kinolarni ko'rish
- `🎭 Janrlar` - Janr bo'yicha tanlash
- `ℹ️ Bot haqida` - Bot haqida ma'lumot

### Admin uchun:

- `/admin` - Admin panelni ochish
- `➕ Kino qo'shish` - Yangi kino qo'shish
- `🗑 Kino o'chirish` - Kinoni o'chirish
- `📊 Statistika` - To'liq statistika ko'rish

## 📁 Loyiha strukturasi

```
kino_bot/
│
├── main.py                 # Asosiy fayl
├── config.py              # Konfiguratsiya
├── requirements.txt       # Python kutubxonalari
├── .env                   # Muhit o'zgaruvchilari (yaratiladi)
├── .env.example          # .env namunasi
├── .gitignore            # Git ignore qoidalari
├── README.md             # Hujjat (bu fayl)
│
├── handlers/             # Handlerlar
│   ├── __init__.py
│   ├── user_handlers.py      # Foydalanuvchi handlerlari
│   ├── admin_handlers.py     # Admin handlerlari
│   └── callback_handlers.py  # Callback handlerlari
│
├── keyboards/            # Klaviaturalar
│   ├── __init__.py
│   ├── reply.py              # Reply klaviaturalar
│   └── inline.py             # Inline klaviaturalar
│
└── database/            # Ma'lumotlar bazasi
    ├── __init__.py
    └── models.py            # Database modellari

```

## 🗄 Database strukturasi

### `movies` jadvali
- `id` - Kino ID (PRIMARY KEY)
- `title` - Kino nomi (inglizcha)
- `title_uz` - Kino nomi (o'zbekcha)
- `year` - Yili
- `genre` - Janr
- `rating` - Reyting (0-10)
- `description` - Tavsif
- `file_id` - Telegram file ID
- `file_type` - Fayl turi (video/document)
- `added_by` - Qo'shgan admin ID
- `added_date` - Qo'shilgan vaqt

### `users` jadvali
- `user_id` - Foydalanuvchi ID (PRIMARY KEY)
- `username` - Username
- `first_name` - Ism
- `last_name` - Familiya
- `is_admin` - Admin ekanmi
- `join_date` - Qo'shilgan sana
- `last_activity` - Oxirgi faollik

### `search_history` jadvali
- `id` - ID (PRIMARY KEY)
- `user_id` - Foydalanuvchi ID
- `query` - Qidiruv so'rovi
- `search_date` - Qidiruv sanasi

## 🛠 Texnologiyalar

- **Python 3.8+** - Dasturlash tili
- **aiogram 3.4.1** - Telegram Bot API kutubxonasi
- **aiosqlite 0.19.0** - Asinxron SQLite
- **environs 10.3.0** - Muhit o'zgaruvchilari boshqaruvi
- **python-dotenv 1.0.0** - .env fayl yuklash

## 🔧 Sozlash va moslashtirish

### Yangi janr qo'shish

`keyboards/inline.py` faylida `get_genre_keyboard()` funksiyasini tahrirlang:

```python
genres = [
    ("🎬 Aksiya", "genre_action"),
    # Yangi janr qo'shing
    ("🎸 Musikal", "genre_musical"),
]
```

### Admin qo'shish

`.env` faylida `ADMIN_IDS` ga yangi ID qo'shing:

```env
ADMIN_IDS=123456789,987654321,111222333
```

## 🐛 Muammolarni hal qilish

### Bot ishlamayapti

1. `.env` faylini tekshiring - token to'g'rimi?
2. Internet aloqasini tekshiring
3. Python versiyasini tekshiring: `python --version`
4. Kutubxonalar o'rnatilganmi: `pip list`

### Database xatoligi

Database faylini o'chirib, qayta ishga tushiring:

```bash
rm kino_bot.db
python main.py
```

### Kino yuklanmayapti

- Fayl hajmi 50MB dan oshmasin (Telegram limit)
- Video formatini tekshiring (MP4 tavsiya etiladi)
- File ID to'g'ri saqlanganmi

## 📝 Litsenziya

MIT License

## 👨‍💻 Muallif

Telegram: @your_username

## 🤝 Hissa qo'shish

Pull request'lar qabul qilinadi! Katta o'zgarishlar uchun avval issue oching.

## 📞 Aloqa

Savollar va takliflar uchun:
- Telegram: @your_admin
- GitHub Issues: [Issues](https://github.com/john0099123h-hash/islomaka/issues)

---

⭐️ Agar loyiha yoqsa, GitHub'da star bering!
