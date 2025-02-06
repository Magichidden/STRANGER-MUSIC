import math
from pyrogram.types import InlineKeyboardButton
from SHUKLAMUSIC import app
import config
from SHUKLAMUSIC.utils.formatters import time_to_seconds

def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="IIمکث", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▷ادامه", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="‣‣Iبعدی", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="◢بیصدا", callback_data=f"ADMIN Mute|{chat_id}"),
            InlineKeyboardButton(text="◣باصدا", callback_data=f"ADMIN Sound|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="≡پلی لیست", callback_data=f"ADMIN Playlist|{chat_id}"),
            InlineKeyboardButton(text="▢توقف", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="𝙍𝘼𝙉𝙂𝙀𝙍 ™", url="https://t.me/TG_GP_IRAN")],
        [InlineKeyboardButton(text="×بستن", callback_data="close")],
    ]
    return buttons

def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    
    if 0 < umm <= 10:
        bar = "○───────────"
    elif 10 < umm < 20:
        bar = "─●──────────"
    elif 20 <= umm < 30:
        bar = "──●─────────"
    elif 30 <= umm < 40:
        bar = "───●────────"
    elif 40 <= umm < 50:
        bar = "────●───────"
    elif 50 <= umm < 60:
        bar = "─────●──────"
    elif 60 <= umm < 70:
        bar = "──────●─────"
    elif 70 <= umm < 80:
        bar = "───────●────"
    elif 80 <= umm < 95:
        bar = "────────●───"
    else:
        bar = "─────────●──"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="IIمکث", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▷ادامه", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="‣‣Iبعدی", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="◢بیصدا", callback_data=f"ADMIN Mute|{chat_id}"),
            InlineKeyboardButton(text="◣باصدا", callback_data=f"ADMIN Sound|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="≡پلی لیست", callback_data=f"ADMIN Playlist|{chat_id}"),
            InlineKeyboardButton(text="▢توقف", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="𝙍𝘼𝙉𝙂𝙀𝙍 ™", url="https://t.me/TG_GP_IRAN")],
        [InlineKeyboardButton(text="×بستن", callback_data="close")],
    ]
    return buttons

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="▷▷",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [InlineKeyboardButton(text="𝙍𝘼𝙉𝙂𝙀𝙍 ™", url="https://t.me/TG_GP_IRAN")],
        [
            InlineKeyboardButton(
                text="×",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="▷▷",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◄",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(text="𝙍𝘼𝙉𝙂𝙀𝙍 ™", url="https://t.me/GANZH"),
            InlineKeyboardButton(
                text="►",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="×",
                callback_data=f"forceclose {query}|{user_id}",
            ),
        ],
    ]
    return buttons
