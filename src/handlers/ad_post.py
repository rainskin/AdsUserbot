from pyrogram import filters, types

import config
import lib
from core import bot


@bot.on_message(filters.channel)
def forward_ad_post(_, msg: types.Message):
    urls = lib.urls.parse(msg)

    for url in urls:
        if lib.blacklist.allowed(url):
            msg.forward(config.ADMIN_CHAT_ID)
            break
