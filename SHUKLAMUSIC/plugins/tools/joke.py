import requests
from SHUKLAMUSIC import app
from pyrogram import Client, filters

JOKE_API_ENDPOINT = 'https://open.wiki-api.ir/api/v1/jokes/random'

@app.on_message(filters.command(["joke", "جوک"], prefixes=["/", "!", "."]))
async def joke(_, message):
    try:
        # ارسال درخواست به API
        response = requests.get(JOKE_API_ENDPOINT)
        response.raise_for_status()  # بررسی خطاهای احتمالی
        
        # دریافت داده‌های JSON
        joke_data = response.json()
        
        # استخراج متن جوک
        joke_text = joke_data.get('text', 'متاسفانه جوکی یافت نشد!')
        
        # ارسال جوک به همراه کپشن
        await message.reply_text(
            f"😂 جوک:\n\n{joke_text}\n\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
            "🤖 @atrinmusic_tm1"
        )
        
    except requests.exceptions.RequestException as e:
        # مدیریت خطاهای احتمالی
        await message.reply_text(
            "❌ متاسفانه در دریافت جوک مشکلی پیش آمده است.\n"
            "لطفاً کمی بعد دوباره تلاش کنید."
        )
        print(f"Error fetching joke: {e}")

# اضافه کردن دستور برای دریافت جوک های بیشتر
@app.on_message(filters.command(["jokes", "جوک_ها"], prefixes=["/", "!", "."]))
async def multiple_jokes(_, message):
    try:
        # تعداد جوک‌های درخواستی (پیش‌فرض: 3)
        count = 3
        jokes_list = []
        
        # دریافت چند جوک
        for _ in range(count):
            response = requests.get(JOKE_API_ENDPOINT)
            response.raise_for_status()
            joke_data = response.json()
            jokes_list.append(joke_data.get('text', ''))
        
        # ساخت متن پیام
        jokes_text = "\n\n➖➖➖➖➖\n\n".join(
            f"😂 {i+1}. {joke}" for i, joke in enumerate(jokes_list)
        )
        
        # ارسال جوک‌ها
        await message.reply_text(
            f"🎯 چند تا جوک باحال:\n\n{jokes_text}\n\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
            "🤖 @atrinmusic_tm1"
        )
        
    except requests.exceptions.RequestException as e:
        await message.reply_text(
            "❌ متاسفانه در دریافت جوک‌ها مشکلی پیش آمده است.\n"
            "لطفاً کمی بعد دوباره تلاش کنید."
        )
        print(f"Error fetching jokes: {e}")
