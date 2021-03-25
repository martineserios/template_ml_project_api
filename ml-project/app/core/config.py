from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")


APP_VERSION: str = config("APP_VERSION", cast=str)
APP_NAME: str = config("APP_NAME", cast=str)
API_PREFIX = "/api"


API_KEY: Secret = config("API_KEY", cast=Secret)#, default= '')
IS_DEBUG: bool = config("IS_DEBUG", cast=bool)#, default=True)
MODELS_PATH: str = config("MODELS_PATH", cast=str)


PREDICT_MODEL_PATH: str = f'{MODELS_PATH}/classLSVC_p.pickle'
PRE_PROC_MODEL_PATH: str = f'{MODELS_PATH}/TfidfVectorizer_p.pickle'