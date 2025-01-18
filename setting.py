import os

DEBUG = os.getenv("DEVELOPMENT", False)

if DEBUG:
    print("In development")
    from pathlib import Path
    from dotenv import load_dotenv
    env_path = Path(".") / ".env.develop"
    load_dotenv(dotenv_path=env_path)
    from settings.development import *
else:
    print("In production")
    from settings.production import *