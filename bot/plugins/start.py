from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
    
    if not await c.db.is_user_exist(m.chat.id):
        await c.db.add_user(m.chat.id)
        await c.send_message(
            Config.LOG_CHANNEL,
            f"New User [{m.from_user.first_name}](tg://user?id={m.chat.id}) started."
        )
    
    await m.reply_text(
        text=f"Hi 👋 there {m.from_user.mention}.\n\nI'm Screenshot Generator Bot. I can provide screenshots from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.\n\n🚨 Porn Contents "
        "will be gives you PERMANENT BAN 🚨\n\n🍃 Bᴏᴛ Made Bʏ :@MHND_KDR",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🍬 Project channel', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL'),
                    InlineKeyboardButton('🍭 Support group', url='https://telegram.me/MHND_BOT_UPDATE_GROUP')
                ],
                [
                    InlineKeyboardButton('🌹 Source code 🌹', url='https://github.com/github2tg/FILE_ANIMATING'),
                    InlineKeyboardButton('👩‍💻 Master', url='https://telegram.me/MHND_KDR')
                ]
            ]
        )
    )
