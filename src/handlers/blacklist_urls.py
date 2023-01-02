from pyrogram import filters, types

import config
import lib
import models
from core import bot


@bot.on_message(filters.chat(config.BLACKLIST_URLS_CHAT_ID))
def save_blacklist_urls(_, message: types.Message):
    new_urls = lib.urls.parse(message)
    saved_urls = {i.value for i in models.BlacklistUrl.get_docs()}

    for url in new_urls:
        if url not in saved_urls:
            models.BlacklistUrl(value=url).save()
