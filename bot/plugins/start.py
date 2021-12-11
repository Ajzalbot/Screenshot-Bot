from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"𝑯𝒊 👋 𝒕𝒉𝒆𝒓𝒆 {m.from_user.mention}.\n\n𝑰'𝒎 𝑺𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒐𝒓 𝑩𝒐𝒕.\n\n𝗦𝗲𝗻𝗱 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲 𝘆𝗼𝘂 "
        "𝘄𝗮𝗻𝘁 𝘁𝗼👉 [TᕼIՏ ᗷOT](tg://resolve?domain=BEST_FILE_STREAM_BOT).\n𝗧𝗵𝗲𝗻 𝗽𝗮𝘀𝘁𝗲 𝘁𝗵𝗲 👉 [ᒪIᑎK ᕼᗴᖇᗴ](tg://resolve?domain=SCREEN_SHOT_ROBOT)\n\n𝙁𝙤𝙧 𝙢𝙤𝙧𝙚 "
        "𝙙𝙚𝙩𝙖𝙞𝙡𝙨 𝙘𝙝𝙚𝙘𝙠 /help.\n\n🚨 𝗣𝗼𝗿𝗻 𝗖𝗼𝗻𝘁𝗲𝗻𝘁𝘀 "
        "𝐰𝐢𝐥𝐥 𝐛𝐞 𝐠𝐢𝐯𝐞𝐬 𝐲𝐨𝐮 𝙋𝙀𝙍𝙈𝘼𝙉𝙀𝙉𝙏 𝘽𝘼𝙉 🚨\n\n🍃 Bᴏᴛ Made Bʏ :@MHND_KDR",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🍬 ℙ𝕣𝕠𝕛𝕖𝕔𝕥 𝕔𝕙𝕒𝕟𝕟𝕖𝕝', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL'),
                    InlineKeyboardButton('🍭 𝕊𝕦𝕡𝕡𝕠𝕣𝕥 𝕘𝕣𝕠𝕦𝕡', url='https://telegram.me/MHND_BOT_UPDATE_GROUP')
                ],
                [
                    InlineKeyboardButton('🌹 𝕊𝕠𝕦𝕣𝕔𝕖 𝕔𝕠𝕕𝕖', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL/145'),
                    InlineKeyboardButton('👩‍💻 𝕄𝕒𝕤𝕥𝕖𝕣', url='https://telegram.me/MHND_KDR')
                ]
            ]
        )
    )
