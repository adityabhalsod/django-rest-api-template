# settings.py
from dotenv import load_dotenv

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


import os

from .common import *

if os.getenv("ENVIRONMENT") == "local":  # local development
    from .local import * # noqa
elif os.getenv("ENVIRONMENT") == "staging":  # staging development
    from .staging import *
else:  # production
    from .production import *

