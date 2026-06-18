# 🎨 Modern Portfolio Website

Professional va zamonaviy portfolio sayti - **sanokulov.uz** saytidan ilhomlangan!

## ✨ Xususiyatlari

- 🎭 **Zamonaviy Dizayn** - Gradient ranglar va smooth animatsiyalar
- 📱 **To'liq Responsive** - Barcha qurilmalarda mukammal ko'rinish
- 🌓 **Dark Mode** - Qorong'u va yorug' rejim
- ⚡️ **Tez Yuklanish** - Optimizatsiya qilingan kod
- 🎯 **Smooth Scrolling** - Yumshoq sahifa o'tishlari
- ✍️ **Typing Effect** - Animatsiyali matn effekti
- 🎨 **Portfolio Filter** - Loyihalarni kategoriya bo'yicha filterlash
- 📊 **Skills Animation** - Animatsiyali ko'nikmalar diagrammasi
- 📧 **Contact Form** - Aloqa formasi
- 🔝 **Back to Top** - Yuqoriga qaytish tugmasi

## 🚀 O'rnatish

### 1. Loyihani yuklab oling

```bash
git clone https://github.com/john0099123h-hash/islomaka.git
cd islomaka/portfolio-website
```

### 2. Fayllarni tahrirlang

`index.html` faylida shaxsiy ma'lumotlaringizni o'zgartiring:

```html
<!-- Ismingizni o'zgartiring -->
<h1>Hi, I'm <span class="gradient-text">Sizning Ismingiz</span></h1>

<!-- Email -->
<strong>sizning.email@example.com</strong>

<!-- Telefon -->
<strong>+998 XX XXX XX XX</strong>

<!-- Social media linklar -->
<a href="https://github.com/sizning-username">GitHub</a>
<a href="https://t.me/sizning-username">Telegram</a>
```

### 3. Rasmlarni qo'shing

`images/` papkasiga quyidagi rasmlarni qo'ying:

- `profile.jpg` - Profil rasmi (Hero section)
- `about.jpg` - About section rasmi
- `project1.jpg` - Loyiha 1 rasmi
- `project2.jpg` - Loyiha 2 rasmi
- ... va hokazo

**Eslatma:** Agar rasmlaringiz yo'q bo'lsa, [Unsplash](https://unsplash.com/) yoki [Pexels](https://www.pexels.com/) dan bepul rasmlar yuklab olishingiz mumkin.

### 4. Brauzerda ochish

Oddiy ravishda `index.html` faylini brauzerda oching yoki Live Server ishlatib ko'ring.

## 📁 Loyiha strukturasi

```
portfolio-website/
│
├── index.html              # Asosiy HTML fayl
│
├── css/
│   └── style.css          # Barcha CSS stillar
│
├── js/
│   └── script.js          # JavaScript kodlar
│
├── images/                # Rasmlar papkasi
│   ├── profile.jpg
│   ├── about.jpg
│   └── project*.jpg
│
├── assets/                # Boshqa fayllar (CV, ikonkalar)
│
└── README.md             # Hujjat (bu fayl)
```

## 🎨 Ranglarni o'zgartirish

`css/style.css` faylining boshidagi `--primary-color`, `--secondary-color` va `--accent-color` o'zgaruvchilarini o'zgartiring:

```css
:root {
    --primary-color: #6366f1;     /* Asosiy rang */
    --secondary-color: #8b5cf6;   /* Ikkinchi rang */
    --accent-color: #ec4899;      /* Urg'u rang */
}
```

## 🔧 Sozlash

### Typing Effect matnlarini o'zgartirish

`js/script.js` faylida:

```javascript
const texts = [
    'Sizning kasabingiz 1',
    'Sizning kasabingiz 2',
    'Sizning kasabingiz 3',
    'Sizning kasabingiz 4'
];
```

### Skills foizlarini o'zgartirish

`index.html` faylida har bir skill uchun `data-progress` attributini o'zgartiring:

```html
<div class="skill-progress" data-progress="95"></div>
```

### Services qo'shish yoki o'chirish

`index.html` dagi Services section'ida `.service-card` qo'shing yoki o'chiring.

## 📤 Hostingga joylashtirish

### GitHub Pages

1. GitHub'da repository yarating
2. Barcha fayllarni yuklang
3. Settings → Pages → Source: main branch
4. `https://username.github.io/repository-name` da ko'ring

### Netlify

1. [Netlify](https://www.netlify.com/) da ro'yxatdan o'ting
2. Loyiha papkasini drag & drop qiling
3. Avtomatik deploy bo'ladi!

### Vercel

1. [Vercel](https://vercel.com/) da ro'yxatdan o'ting
2. GitHub repo'ni ulang
3. Deploy tugmasini bosing

## 🌟 Keyingi qadamlar

- ✅ Shaxsiy ma'lumotlarni kiriting
- ✅ Rasmlarni qo'shing
- ✅ Loyihalar qo'shing
- ✅ CV faylini qo'shing
- ✅ Hostingga joylashtiring
- ✅ Google Analytics qo'shing (ixtiyoriy)
- ✅ SEO optimization (ixtiyoriy)

## 🛠 Texnologiyalar

- **HTML5** - Markup tili
- **CSS3** - Stillar (Flexbox, Grid, Animations)
- **JavaScript (Vanilla)** - Funksionallik
- **Font Awesome** - Ikonkalar
- **Google Fonts** - Inter font

## 💡 Maslahatlar

1. **Rasmlar hajmi:** Rasmlarni [TinyPNG](https://tinypng.com/) da siqib optimizatsiya qiling
2. **SEO:** Meta taglar va description qo'shing
3. **Analytics:** Google Analytics qo'shing
4. **SSL:** HTTPS ishlatayotganingizga ishonch hosil qiling
5. **Performance:** [PageSpeed Insights](https://pagespeed.web.dev/) da tekshiring

## 🎯 Demo

🌐 **Live Demo:** [Ko'rish](https://your-demo-link.com)

## 📸 Screenshot

![Portfolio Screenshot](screenshot.png)

## 📞 Aloqa

Savollar yoki takliflaringiz bo'lsa:

- 📧 Email: your.email@example.com
- 💬 Telegram: [@yourusername](https://t.me/yourusername)
- 🐙 GitHub: [@yourusername](https://github.com/yourusername)

## 📄 Litsenziya

MIT License - xohlagan maqsadda erkin foydalanishingiz mumkin!

## 🙏 Minnatdorchilik

Bu sayt [sanokulov.uz](https://www.sanokulov.uz/) saytidan ilhomlangan.

---

⭐️ Agar loyiha yoqsa, GitHub'da star bering!

**Made with ❤️ by Your Name**
