from envparse import env

env.read_envfile()

API_ID = env('API_ID')
API_HASH = env('API_HASH')
ADMIN_CHAT_ID = -1001738507553

BLACKLIST_URLS = env.list('BLACKLIST_URLS')
