from fastapi import APIRouter, Depends
from starlette.requests import Request

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

    model: Model = request.app.state.model
    output: OutputTemplate = model.predict(input)

    return output
