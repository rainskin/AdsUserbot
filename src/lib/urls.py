from pyrogram import types
from pyrogram.enums import MessageEntityType


def _parse_entity(text: str, entity: types.MessageEntity) -> str | None:
    url = None

    if entity.type == MessageEntityType.TEXT_LINK:
        url = entity.url
    elif entity.type == MessageEntityType.MENTION:
        url = 'https://t.me/' + text[entity.offset + 1:entity.offset + entity.length]
    elif entity.type == MessageEntityType.URL:
        url = text[entity.offset:entity.offset + entity.length]

    if not url:
        return None

    if not url.startswith('http'):
        url = 'https://' + url

    return url.replace('http://', 'https://')


def parse(msg: types.Message) -> list[str]:
    text = msg.text or msg.caption
    entities = msg.entities or msg.caption_entities or []
    urls_raw = {_parse_entity(text, e) for e in entities}
    return [i for i in urls_raw if i]
