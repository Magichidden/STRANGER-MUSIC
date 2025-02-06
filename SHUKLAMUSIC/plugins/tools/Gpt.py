import requests
from SHUKLAMUSIC import app
from pyrogram.types import Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

API_KEY = "abacf43bf0ef13f467283e5bc03c2e1f29dae4228e8c612d785ad428b32db6ce"

BASE_URL = "https://api.together.xyz/v1/chat/completions"

@app.on_message(
    filters.command(
        ["chatgpt", "ai","هی ربات", "ask", "gpt", "solve"],
        prefixes=["+", ".", "/", "-", "", "$", "#", "&"],
    )
)
async def chat_gpt(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "❍ مثال:**\n\n/chatgpt صاحب ˹ آترین موزیک ™˼ کیست؟"
            )
        else:
            query = message.text.split(' ', 1)[1]
            print("سوال ورودی:", query)

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            }

            response = requests.post(BASE_URL, json=payload, headers=headers)

            print("پاسخ API:", response.text)
            print("کد وضعیت:", response.status_code)

            if response.status_code != 200:
                await message.reply_text(f"❍ خطا: درخواست API ناموفق بود. کد وضعیت: {response.status_code}")
            elif not response.text.strip():
                await message.reply_text("❍ خطا: هیچ داده معتبری از API دریافت نشد. پاسخ خالی بود.")
            else:
                try:
                    response_data = response.json()
                    print("پاسخ JSON از API:", response_data)

                    if "choices" in response_data and len(response_data["choices"]) > 0:
                        result = response_data["choices"][0]["message"]["content"]
                        await message.reply_text(
                            f"{result} \n\nپاسخ داده شده توسط➛[˹ آترین موزیک ™˼](https://t.me/atrinmusic_tm1)",
                            parse_mode=ParseMode.MARKDOWN
                        )
                    else:
                        await message.reply_text("❍ خطا: پاسخی از API دریافت نشد.")
                except ValueError:
                    await message.reply_text("❍ خطا: فرمت پاسخ نامعتبر است.")
    except Exception as e:
        await message.reply_text(f"**❍ خطا: {e} ")
