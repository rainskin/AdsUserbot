from core import env

ADMIN_CHAT_ID = env.get_int('ADMIN_CHAT_ID')
BLACKLIST_URLS_CHAT_ID = env.get_int('BLACKLIST_URLS_CHAT_ID')
BLACKLIST_URL_REGEXPS = [r'.*telegra.ph.*', '.*t.me/addstickers.*', '.*teletype.in.*']
