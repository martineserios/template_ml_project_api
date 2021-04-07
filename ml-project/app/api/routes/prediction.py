from fastapi import APIRouter, Depends
from starlette.requests import Request
import time
from loguru import logger

from app.core import security
from app.models.input import InputModel
from app.models.output import OutputModel
from app.services.models import Model

router = APIRouter()


@router.post("/predict", response_model=OutputModel, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = True,#Depends(security.validate_request),
    input: InputModel = None
) -> OutputModel:
    start_time = time.time()

    model: Model = request.app.state.model
    output: OutputModel = model.predict(input)

    logger.info("PREDICTION TIME: %s seconds." % (time.time() - start_time))

    return output
