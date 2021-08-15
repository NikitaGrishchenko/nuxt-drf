from .common import BACKEND_DIR
from .environment import env

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BACKEND_DIR / "db.sqlite3",
    }
}


SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ["*"]

