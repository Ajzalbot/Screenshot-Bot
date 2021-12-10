import datetime

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..utils import Utilities
from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_message(
    filters.private
    & ((filters.text & ~filters.edited) | filters.media)
    & filters.incoming
)
async def _(c, m):

    if m.media:
        if not Utilities.is_valid_file(m):
            return
    else:
        if not Utilities.is_url(m.text):
            return

    snt = await m.reply_text(
        "Hi there, Please wait while I'm getting everything ready to process your request!",
        quote=True,
    )

    if m.media:
        file_link = Utilities.generate_stream_link(m)
    else:
        file_link = m.text

    duration = await Utilities.get_duration(file_link)
    if isinstance(duration, str):
        await snt.edit_text("😢 Sorry! I cannot open the file.")
        log = await m.forward(Config.LOG_CHANNEL)
        await log.reply_text(duration, True)
        return

    btns = Utilities.gen_ik_buttons()

    if duration >= 600:
        btns.append([InlineKeyboardButton("📸Generate Sample Video📸", "smpl")])

    await snt.edit_text(
        text=f"👋𝙃𝙞, 𝘾𝙝𝙤𝙤𝙨𝙚 𝙤𝙣𝙚 𝙤𝙛 𝙩𝙝𝙚 𝙤𝙥𝙩𝙞𝙤𝙣𝙨.\n𝙏𝙤𝙩𝙖𝙡 𝙙𝙪𝙧𝙖𝙩𝙞𝙤𝙣: `{datetime.timedelta(seconds=duration)}` (`{duration}s`)",
        reply_markup=InlineKeyboardMarkup(btns),
    )
