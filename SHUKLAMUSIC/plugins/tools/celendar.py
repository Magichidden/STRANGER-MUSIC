from pyrogram import Client, filters
from PIL import Image, ImageEnhance
from io import BytesIO
import aiohttp
import calendar
import jdatetime
from SHUKLAMUSIC import app

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image_data = await resp.read()

    carbon_image = Image.open(BytesIO(image_data))
    enhancer = ImageEnhance.Brightness(carbon_image)
    bright_image = enhancer.enhance(1.7)

    output_image = BytesIO()
    bright_image.save(output_image, format='PNG', quality=95)
    output_image.name = "carbon.png"
    return output_image

def get_persian_month_name(month):
    persian_months = {
        1: "فروردین",
        2: "اردیبهشت",
        3: "خرداد",
        4: "تیر",
        5: "مرداد",
        6: "شهریور",
        7: "مهر",
        8: "آبان",
        9: "آذر",
        10: "دی",
        11: "بهمن",
        12: "اسفند"
    }
    return persian_months.get(month, "")

def generate_persian_calendar(year):
    calendar_text = f"تقویم سال {year} شمسی\n\n"
    
    for month in range(1, 13):
        jd = jdatetime.date(year, month, 1)
        month_name = get_persian_month_name(month)
        calendar_text += f"\n{month_name}\n"
        calendar_text += "شنبه  یکشنبه  دوشنبه  سه‌شنبه  چهارشنبه  پنج‌شنبه  جمعه\n"
        
        # Find the first day of the month
        first_day = jd.weekday()
        
        # Add spacing for the first week
        calendar_text += "   " * first_day
        
        # Add days
        for day in range(1, jdatetime.monthrange(year, month)[1] + 1):
            calendar_text += f"{day:2d}".rjust(4)
            if (first_day + day) % 7 == 0:
                calendar_text += "\n"
        calendar_text += "\n"
    
    return calendar_text

@app.on_message(filters.command(["calendar", "تقویم"], prefixes=["/", "!", "."]))
async def send_calendar(_, message):
    command_parts = message.text.split(" ")
    if len(command_parts) == 2:
        try:
            year = int(command_parts[1])
        except ValueError:
            await message.reply("لطفا سال معتبر وارد کنید. مثال: /تقویم 1402")
            return
    else:
        # Default to current Iranian year if no year is specified
        current_jyear = jdatetime.datetime.now().year
        year = current_jyear

    # Generate Persian calendar
    persian_calendar = generate_persian_calendar(year)
    
    # Generate the Carbon image for the calendar
    carbon_image = await make_carbon(persian_calendar)
    
    # Send the image as a reply to the user
    await app.send_photo(
        message.chat.id,
        carbon_image,
        caption=f"📅 تقویم سال {year} شمسی\n➖➖➖➖➖➖➖➖➖➖\n🤖 @atrinmusic_tm1"
    )

@app.on_message(filters.command(["month", "ماه"], prefixes=["/", "!", "."]))
async def send_current_month(_, message):
    current_date = jdatetime.datetime.now()
    year = current_date.year
    month = current_date.month
    
    # Generate current month calendar
    calendar_text = f"تقویم {get_persian_month_name(month)} {year}\n\n"
    jd = jdatetime.date(year, month, 1)
    
    calendar_text += "شنبه  یکشنبه  دوشنبه  سه‌شنبه  چهارشنبه  پنج‌شنبه  جمعه\n"
    
    first_day = jd.weekday()
    calendar_text += "   " * first_day
    
    for day in range(1, jdatetime.monthrange(year, month)[1] + 1):
        calendar_text += f"{day:2d}".rjust(4)
        if (first_day + day) % 7 == 0:
            calendar_text += "\n"
    
    carbon_image = await make_carbon(calendar_text)
    
    await app.send_photo(
        message.chat.id,
        carbon_image,
        caption=f"📅 تقویم {get_persian_month_name(month)} ماه {year}\n➖➖➖➖➖➖➖➖➖➖\n🤖 @atrinmusic_tm1"
    )

@app.on_message(filters.command(["date", "تاریخ"], prefixes=["/", "!", "."]))
async def send_today_date(_, message):
    today = jdatetime.datetime.now()
    persian_weekdays = {
        0: "شنبه",
        1: "یکشنبه",
        2: "دوشنبه",
        3: "سه‌شنبه",
        4: "چهارشنبه",
        5: "پنج‌شنبه",
        6: "جمعه"
    }
    weekday = persian_weekdays[today.weekday()]
    
    date_text = f"امروز: {weekday}\n{today.day} {get_persian_month_name(today.month)} {today.year}"
    
    await message.reply_text(
        f"📅 تاریخ امروز:\n{date_text}\n➖➖➖➖➖➖➖➖➖➖\n🤖 @atrinmusic_tm1"
    )
