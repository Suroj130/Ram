from pyrogram import Client
# ১. প্রথমে ইম্পোর্ট করুন (ফাইলের একদম উপরে)
from BrandrdXMusic.utils.flood_control import flood_protect

# ২. প্রতিটি কমান্ডের ঠিক আগে @flood_protect বসান
@Client.on_message(filters.command("start"))
@flood_protect                    # এই লাইনটা যোগ করুন
async def start_command(client, message):
    await message.reply("বট চালু আছে!")
from pyrogram.types import InlineKeyboardButton

import config
from BrandrdXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_7"], callback_data="gib_source")
        ],
    ]
    return buttons
