from fastapi import APIRouter, Depends
from starlette.requests import Request
import time
<<<<<<< HEAD
###
from app.logging import logger
# Gets or creates a logger
logger = logger.getChild(__name__)  
=======
>>>>>>> b9fc5da560209a07695a0ab181c701e416b4aead

from app.core import security
from app.templates.input import InputTemplate
from app.templates.output import OutputTemplate
from app.services.models import Model

from app.logging import logger
# Gets or creates a logger
logger = logger.getChild(__name__)  

from app.core import security
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


    logger.debug(f"Campaña: '{input.campaign_name}' | id_survey_response: '{input.id_survey_response}' | PREDICTION TIME: {time.time() - start_time} seconds.")
    logger.debug(f"Campaña: '{input.campaign_name}' | id_survey_response: '{input.id_survey_response}' | SAVE: answer: {input.answer}, categ: {output.categ}, categ_proba: {output.categ_prob}")

    return output
