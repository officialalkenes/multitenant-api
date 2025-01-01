import os
from urllib.parse import urlparse
from .base import *  # noqa

database_url = os.getenv("DATABASE_URL")
if isinstance(database_url, bytes):
    # Decode the bytes-like object to a string
    database_url = database_url.decode("utf-8")

tmpPostgres = urlparse(database_url)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": tmpPostgres.path.replace("/", ""),
        "USER": tmpPostgres.username,
        "PASSWORD": tmpPostgres.password,
        "HOST": tmpPostgres.hostname,
        "PORT": 5432,
    }
}

# Debug mode
DEBUG = True

# Allowed hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
