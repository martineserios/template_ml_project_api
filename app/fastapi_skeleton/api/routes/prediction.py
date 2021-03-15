from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.core import security
from app.models.answer import AnswerTranscription
from app.models.prediction import AnswerCategory
from app.services.models import AnswerClassifierModel

router = APIRouter()


@router.post("/predict", response_model=AnswerCategory, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    answer: AnswerTranscription = None
) -> AnswerCategory:

    model: AnswerClassifierModel = request.app.state.model
    prediction: AnswerCategory = model.predict(answer)

    return prediction
