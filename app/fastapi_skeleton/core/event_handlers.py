

from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.core.config import PREDICT_MODEL_PATH
from app.core.config import PRE_PROC_MODEL_PATH
from app.services.models import AnswerClassifierModel


def _startup_model(app: FastAPI) -> None:
    predict_model_path = PREDICT_MODEL_PATH
    pre_proc_model_path = PRE_PROC_MODEL_PATH
    
    model_instance = AnswerClassifierModel(predict_model_path, pre_proc_model_path)

    app.state.model = model_instance


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)
    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)
    return shutdown
