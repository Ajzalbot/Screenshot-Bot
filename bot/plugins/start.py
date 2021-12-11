from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hi 👋 there {m.from_user.mention}.\n\nI'm Screenshot Generator Bot.\n\nSend the file you "
        "want to👉 [this bot](tg://resolve?domain=BEST_FILE_STREAM_BOT).\nThen paste the👉 [link here](tg://resolve?domain=SCREEN_SHOT_ROBOT)\n\nFor more "
        "details check /help.\n\n🚨 Porn Contents "
        "will be gives you PERMANENT BAN 🚨\n\n🍃 Bᴏᴛ Made Bʏ :@MHND_KDR",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🍬 Project channel', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL'),
                    InlineKeyboardButton('🍭 Support group', url='https://telegram.me/MHND_BOT_UPDATE_GROUP')
                ],
                [
                    InlineKeyboardButton('🌹 Source code 🌹', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL/145'),
                    InlineKeyboardButton('👩‍💻 Master', url='https://telegram.me/MHND_KDR')
                ]
            ]
        )
    )
