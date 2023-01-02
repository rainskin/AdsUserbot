from mongoengine import connect

from . import config

connect(
    db=config.MONGO_DB,
    host=config.MONGO_HOST,
    username=config.MONGO_USER,
    password=config.MONGO_PASSWORD,
)
