from pyrogram import filters, types

import config
import lib
import models
from core import bot


@bot.on_message(filters.channel)
def forward_ad_post(_, msg: types.Message):
    urls = lib.urls.parse(msg)
    blacklist_urls = [i.value for i in models.BlacklistUrl.get_docs()]

    for url in urls:
        if url not in blacklist_urls:
            msg.forward(config.ADMIN_CHAT_ID)
            break
