from .env import env

SESSION_PATH = env.get('SESSION_PATH')
API_ID = env.get_int('API_ID')
API_HASH = env.get('API_HASH')
USERBOT_SESSION_STRING = env.get('USERBOT_SESSION_STRING')
PHONE_NUMBER = env.get('PHONE_NUMBER')
PASSWORD = env.get('PASSWORD')

MONGO_DB = env.get('MONGO_DB')
MONGO_HOST = env.get('MONGO_HOST', 'localhost')
MONGO_USER = env.get('MONGO_USER', None)
MONGO_PASSWORD = env.get('MONGO_PASSWORD', None)
