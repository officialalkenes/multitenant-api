from urllib.parse import urlparse
from .base import *  # noqa

tmpPostgres = urlparse(os.getenv("DATABASE_URL"))  # noqa
print(tmpPostgres.hostname)
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
