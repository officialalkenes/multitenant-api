from decouple import config

DJANGO_ENVIRONMENT = config("ENVIRONMENT", "dev")

if DJANGO_ENVIRONMENT == "dev":
    from .dev import *
elif DJANGO_ENVIRONMENT == "prod":
    from .prod import *
# elif ENVIRONMENT == "staging":
#     from .staging import *
else:
    raise ValueError("Invalid environment specified.")