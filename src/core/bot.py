import pyrogram

from . import config


class Bot(pyrogram.Client):
    def __init__(self):
        super().__init__(
            config.SESSION_PATH,
            config.API_ID,
            config.API_HASH,
            phone_number=config.PHONE_NUMBER,
            password=config.PASSWORD,
        )

    def run(self):
        import handlers
        handlers.setup()
        super().run()


bot = Bot()
