from decouple import config

DJANGO_ENVIRONMENT = config("ENVIRONMENT", "dev")

if DJANGO_ENVIRONMENT == "dev":
    from .dev import *  # noqa: F403
elif DJANGO_ENVIRONMENT == "prod":
    from .prod import *  # noqa: F403
# elif ENVIRONMENT == "staging":
#     from .staging import * # noqa: F403
else:
    raise ValueError("Invalid environment specified.")
