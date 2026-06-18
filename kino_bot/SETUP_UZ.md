# 🚀 Kino Bot - Tezkor O'rnatish Yo'riqnomasi

## 1️⃣ Bot yaratish (@BotFather)

1. Telegram'da [@BotFather](https://t.me/BotFather) ni oching
2. `/newbot` yuboring
3. Bot nomini kiriting (masalan: `Mening Kino Botim`)
4. Username kiriting (masalan: `my_kino_bot`)
5. **Token'ni saqlang!** (masalan: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

## 2️⃣ User ID ni olish

1. [@userinfobot](https://t.me/userinfobot) ni oching
2. `/start` bosing
3. **ID raqamni nusxalang** (masalan: `123456789`)

## 3️⃣ Loyihani o'rnatish

### Windows

```cmd
# 1. Loyihani yuklab oling
git clone https://github.com/john0099123h-hash/islomaka.git
cd islomaka\kino_bot

# 2. Virtual muhit
python -m venv venv
venv\Scripts\activate

# 3. Kutubxonalar
pip install -r requirements.txt

# 4. .env fayl yaratish
copy .env.example .env

# 5. .env ni notepad bilan oching va to'ldiring
notepad .env
```

### Linux / Mac

```bash
# 1. Loyihani yuklab oling
git clone https://github.com/john0099123h-hash/islomaka.git
cd islomaka/kino_bot

# 2. Virtual muhit
python3 -m venv venv
source venv/bin/activate

# 3. Kutubxonalar
pip install -r requirements.txt

# 4. .env fayl yaratish
cp .env.example .env

# 5. .env ni tahrirlash
nano .env
```

## 4️⃣ .env faylini to'ldirish

```env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
ADMIN_IDS=123456789
```

**Eslatma:** 
- `BOT_TOKEN` - BotFather dan olgan token
- `ADMIN_IDS` - Sizning user ID raqamingiz

## 5️⃣ Botni ishga tushirish

```bash
python main.py
```

Muvaffaqiyatli bo'lsa:
```
✅ Bot ishga tushmoqda...
✅ Database tables created successfully
✅ Bot muvaffaqiyatli ishga tushdi!
```

## 6️⃣ Botni sinab ko'rish

1. Telegram'da botingizni oching
2. `/start` bosing
3. Admin panel: `/admin`
4. Kino qo'shish: `➕ Kino qo'shish` tugmasini bosing

## 🔥 Tez-tez so'raladigan savollar

### ❓ Token qayerdan olaman?

[@BotFather](https://t.me/BotFather) → `/newbot` → token nusxalang

### ❓ User ID qanday topaman?

[@userinfobot](https://t.me/userinfobot) → `/start` → ID ko'rinadi

### ❓ Bot javob bermayapti?

1. Token to'g'rimi? `.env` faylini tekshiring
2. Internet bormi?
3. `python main.py` ni qayta ishga tushiring

### ❓ Admin panel ishlamayapti?

`.env` faylidagi `ADMIN_IDS` ga o'zingizning ID ni qo'shganmisiz?

### ❓ Kino qo'shishda xato?

- Video hajmi 50MB dan oshmasin
- MP4 formatida bo'lsin
- To'g'ri admin ID kiritilganmi?

## 🎯 Keyingi qadamlar

1. ✅ Botni ishga tushiring
2. ✅ Birinchi kinoni qo'shing
3. ✅ Botni do'stlaringizga ulashing
4. ✅ Kinolar bazasini to'ldiring

## 💡 Maslahatlar

- **Serverda ishlatish uchun:** VPS server oling (DigitalOcean, AWS, Heroku)
- **24/7 ishlashi uchun:** `screen` yoki `tmux` dan foydalaning
- **Ko'proq foydalanuvchilar uchun:** PostgreSQL'ga o'tkazing

## 📞 Yordam kerakmi?

Telegram: @your_admin
GitHub: [Issues](https://github.com/john0099123h-hash/islomaka/issues)

---

✨ **Omad tilaymiz!** Botingiz muvaffaqiyatli bo'lsin! 🎬
