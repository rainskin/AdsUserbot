import pyrogram

from . import config


class Bot(pyrogram.Client):
    def __init__(self):
        super().__init__('userbot', session_string=config.USERBOT_SESSION_STRING)
    def run(self):
        import handlers
        handlers.setup()
        super().run()


bot = Bot()
