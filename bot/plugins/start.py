from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"𝑯𝒊\t👋\t𝒕𝒉𝒆𝒓𝒆\t{m.from_user.mention}.\n\n𝑰'𝒎\t𝑺𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕\t𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒐𝒓\t𝑩𝒐𝒕.\n\n𝗦𝗲𝗻𝗱\t𝘁𝗵𝗲\t𝗳𝗶𝗹𝗲\t𝘆𝗼𝘂\t"
        "𝘄𝗮𝗻𝘁\t𝘁𝗼\t👉\t[TᕼIՏ\tᗷOT](tg://resolve?domain=BEST_FILE_STREAM_BOT).\n𝗧𝗵𝗲𝗻\t𝗽𝗮𝘀𝘁𝗲\t𝘁𝗵𝗲\t👉\t[ᒪIᑎK\tᕼᗴᖇᗴ](tg://resolve?domain=SCREEN_SHOT_ROBOT)\n\n𝙁𝙤𝙧\t𝙢𝙤𝙧𝙚\t"
        "𝙙𝙚𝙩𝙖𝙞𝙡𝙨\t𝙘𝙝𝙚𝙘𝙠\t/help.\n\n🚨\t𝗣𝗼𝗿𝗻\t𝗖𝗼𝗻𝘁𝗲𝗻𝘁𝘀\t"
        "𝐰𝐢𝐥𝐥\t𝐛𝐞\t𝐠𝐢𝐯𝐞𝐬\t𝐲𝐨𝐮\t𝙋𝙀𝙍𝙈𝘼𝙉𝙀𝙉𝙏\t𝘽𝘼𝙉\t🚨\n\n🍃\tBᴏᴛ\tMade\tBʏ\t:\t@MHND_KDR",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🍬 ℙ𝕣𝕠𝕛𝕖𝕔𝕥\t𝕔𝕙𝕒𝕟𝕟𝕖𝕝', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL'),
                    InlineKeyboardButton('🍭 𝕊𝕦𝕡𝕡𝕠𝕣𝕥\t𝕘𝕣𝕠𝕦𝕡', url='https://telegram.me/MHND_BOT_UPDATE_GROUP')
                ],
                [
                    InlineKeyboardButton('🌹 𝕊𝕠𝕦𝕣𝕔𝕖\t𝕔𝕠𝕕𝕖', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL/145'),
                    InlineKeyboardButton('👩‍💻 𝕄𝕒𝕤𝕥𝕖𝕣', url='https://telegram.me/MHND_KDR')
                ],
                [
                    InlineKeyboardButton('**𝑯𝒐𝒘/t𝒖𝒔𝒆/t𝒕𝒉𝒊𝒔/t𝒃𝒐𝒕/t🤔**', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL/145')
                ]
            ]
        )
    )
