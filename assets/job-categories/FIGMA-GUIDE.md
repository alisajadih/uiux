# راهنمای ایمپورت گرافیک‌های دسته‌بندی شغلی در Figma

## دو نسخه موجود

### ۱. ایلاستریشن فلت (پیشنهادی)
سبک مدرن flat illustration — مناسب کارت‌های دسته‌بندی سایت

| دسته‌بندی | SVG وکتور | PNG ایلاستریشن | PNG کارت ۴۰۰px |
|-----------|-----------|----------------|----------------|
| طراحی | `illustrations/svg/design.svg` | `illustrations/png/design-ai.png` | `illustrations/png/design-illustration-card.png` |
| بازاریابی | `illustrations/svg/marketing.svg` | `illustrations/png/marketing-ai.png` | `illustrations/png/marketing-illustration-card.png` |
| منابع انسانی | `illustrations/svg/hr.svg` | `illustrations/png/hr-ai.png` | `illustrations/png/hr-illustration-card.png` |
| آموزشی | `illustrations/svg/education.svg` | `illustrations/png/education-ai.png` | `illustrations/png/education-illustration-card.png` |
| برنامه‌نویسی | `illustrations/svg/programming.svg` | `illustrations/png/programming-ai.png` | `illustrations/png/programming-illustration-card.png` |

نسخه SVG فلت (قابل ویرایش): `illustrations/png/*-flat-card.png` و `*-flat@2x.png`

### ۲. آیکون ساده (نسخه قبلی)
| دسته‌بندی | SVG | PNG |
|-----------|-----|-----|
| طراحی | `svg/design.svg` | `png/design.png` |
| بازاریابی | `svg/marketing.svg` | `png/marketing.png` |
| منابع انسانی | `svg/hr.svg` | `png/hr.png` |
| آموزشی | `svg/education.svg` | `png/education.png` |
| برنامه‌نویسی | `svg/programming.svg` | `png/programming.png` |

## پالت رنگ

| نام | Hex | کاربرد |
|-----|-----|--------|
| فیروزه‌ای تیره | `#0D9488` | گرادیان پس‌زمینه |
| فیروزه‌ای | `#14B8A6` | رنگ اصلی |
| فیروزه‌ای روشن | `#2DD4BF` | هایلایت |
| فیروزه‌ای پاستلی | `#5EEAD4` / `#99F6E4` | آکسان |
| بنفش تیره | `#7C3AED` | گرادیان پس‌زمینه |
| بنفش | `#8B5CF6` | رنگ اصلی |
| بنفش روشن | `#A78BFA` | هایلایت |
| بنفش پاستلی | `#C4B5FD` / `#DDD6FE` | آکسان |

## نحوه ایمپورت در Figma

### روش ۱ — SVG (بهترین گزینه)
1. فایل‌های داخل پوشه `svg/` را بکشید و رها کنید (Drag & Drop) روی بوم Figma
2. آیکون‌ها به‌صورت وکتور وارد می‌شوند — قابل تغییر اندازه بدون افت کیفیت
3. گرادیان‌ها و رنگ‌ها در Figma قابل ویرایش هستند

### روش ۲ — PNG
1. برای نمایش در اندازه ۲۰۰×۲۰۰ پیکسل از فایل‌های `png/*.png` استفاده کنید
2. برای Retina / نمایشگرهای با تراکم بالا از `png/*@2x.png` (۴۰۰×۴۰۰) استفاده کنید

### روش ۳ — Place Image
1. یک Frame بسازید (مثلاً ۲۰۰×۲۰۰)
2. `Shift + Ctrl + K` (Mac: `Shift + Cmd + K`) → فایل را انتخاب کنید

## ساخت Color Styles در Figma

1. یک مستطیل با رنگ `#14B8A6` بکشید
2. در پنل Fill روی آیکون Style کلیک کنید → **+** → نام: `Primary/Teal`
3. همین کار را برای `#8B5CF6` با نام `Primary/Purple` تکرار کنید

## ابعاد پیشنهادی در UI

- کارت دسته‌بندی: آیکون ۶۴–۸۰px
- لیست دسته‌ها: آیکون ۴۸px
- هیرو / بنر: آیکون ۱۲۰–۱۶۰px
