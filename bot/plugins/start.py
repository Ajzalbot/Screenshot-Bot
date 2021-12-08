from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hi 👋 there {m.from_user.mention}.\n\nI'm Screenshot Generator Bot. I can provide screenshots from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.\n\n🚨 Porn Contents will be gives you PERMANENT BAN 🚨",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍬 Project channel", url="https://telegram.me/MHND_BOT_UPDATE_CHANNEL"
                    ),
                    InlineKeyboardButton("🍭 Support group", url="https://telegram.me/MHND_BOT_UPDATE_GROUP"),
                ],
                [InlineKeyboardButton("👩‍💻 Master", url="https://telegram.me/MHND_KDR"),
                [InlineKeyboardButton("👩‍💻 Master", url="https://telegram.me/MHND_KDR")],
           ]
        ),
    )
