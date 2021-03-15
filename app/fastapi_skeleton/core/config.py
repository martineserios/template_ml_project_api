

from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.0.1"
APP_NAME = "API Pago-Pasado"
API_PREFIX = "/api"

config = Config(".env")

API_KEY: Secret = config("API_KEY", cast=Secret, default= 'd24a348b-e6af-402b-8f78-26c261c2a1bf')
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=True)

PREDICT_MODEL_PATH: str = config("DEFAULT_MODEL_PATH", default='/app/app/trained_models/classLSVC_p.pickle')
PRE_PROC_MODEL_PATH: str = config("DEFAULT_MODEL_PATH", default='/app/app/trained_models/TfidfVectorizer_p.pickle')