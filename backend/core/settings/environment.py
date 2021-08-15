import os

import environ

PROJECT_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
ENV_FILE = os.path.join(PROJECT_DIR, ".env")

env = environ.Env(
    DEBUG=(bool, True)
)

if os.path.isfile(ENV_FILE):
    env.read_env(ENV_FILE)
