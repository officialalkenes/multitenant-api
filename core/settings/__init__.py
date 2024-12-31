import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


DJANGO_ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")

if DJANGO_ENVIRONMENT == "dev":
    from .dev import *  # noqa: F403
elif DJANGO_ENVIRONMENT == "prod":
    from .prod import *  # noqa: F403
elif DJANGO_ENVIRONMENT == "test":
    from .test_settings import *  # noqa: F403
else:
    raise ValueError("Invalid environment specified.")

print(DJANGO_ENVIRONMENT)
