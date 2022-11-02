from envparse import env

env.read_envfile()

API_ID = env('API_ID')
API_HASH = env('API_HASH')
ADMIN_CHAT_ID = env.int('ADMIN_CHAT_ID')

BLACKLIST_URLS = env.list('BLACKLIST_URLS')
