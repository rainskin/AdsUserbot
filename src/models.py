import mongoengine as me

from core import Document


class BlacklistUrl(Document):
    value: str = me.StringField()
