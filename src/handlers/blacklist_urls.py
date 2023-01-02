from pyrogram import filters, types

import config
import lib
import models
from core import bot


@bot.on_message(filters.chat(config.BLACKLIST_URLS_CHAT_ID))
def save_blacklist_urls(_, msg: types.Message):
    saved_urls = {i.value for i in models.BlacklistUrl.get_docs()}
    new_urls = [i for i in lib.urls.parse(msg) if i not in saved_urls]

    for url in new_urls:
        models.BlacklistUrl(value=url).save()

    urls_text = '\n'.join(new_urls)
    msg.reply_text(f'Добавлены ссылки:\n\n{urls_text}')
