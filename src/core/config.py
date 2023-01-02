from envparse import env

env.read_envfile()

SESSION_PATH = env('SESSION_PATH')
API_ID = env('API_ID')
API_HASH = env('API_HASH')
PHONE_NUMBER = env('PHONE_NUMBER')
PASSWORD = env('PASSWORD')
