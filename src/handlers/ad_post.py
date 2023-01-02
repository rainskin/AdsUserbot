from pyrogram import filters, types
from pyrogram.enums import MessageEntityType

import config
from core import bot


@bot.on_message(filters.channel)
def forward_ad_post(_, message: types.Message):
    text = message.text or message.caption
    entities = message.entities or message.caption_entities or []

    for entity in entities:
        url = None

        if entity.type == MessageEntityType.TEXT_LINK:
            url = entity.url
        elif entity.type == MessageEntityType.MENTION:
            url = 'https://t.me/' + text[entity.offset + 1:entity.offset + entity.length]
        elif entity.type == MessageEntityType.URL:
            url = text[entity.offset:entity.offset + entity.length]

        if (url is not None) and url not in config.BLACKLIST_URLS:
            message.forward(config.ADMIN_CHAT_ID)
            break
