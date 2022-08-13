from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "testing",
    }
}

LOGS_PATH = ""

LOGGING = ""


INTERNAL_IPS = ("127.0.0.1",)
API_KEY = ""
API_KEY_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
