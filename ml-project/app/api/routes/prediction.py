from fastapi import APIRouter, Depends
from starlette.requests import Request
import time
from loguru import logger

from app.core import security
from app.templates.input import InputTemplate
from app.templates.output import OutputTemplate
from app.services.models import Model

router = APIRouter()


@router.post("/predict", response_model=OutputTemplate, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = True,#Depends(security.validate_request),
    input: InputTemplate = None
) -> OutputTemplate:
    start_time = time.time()

    model: Model = request.app.state.model
    output: OutputTemplate = model.predict(input)

    logger.info("PREDICTION TIME: %s seconds." % (time.time() - start_time))

    return output
