from fastapi import APIRouter, Depends
from starlette.requests import Request


from app.core import security
from app.templates.categories import ModelCategories
from app.services.models import CATEGORY_MAP

router = APIRouter()


@router.get("/categories", response_model=ModelCategories, name="categories")
def get_categories(
    # request: Request,
    authenticated: bool = True,#Depends(security.validate_request),
    # answer: AnswerTranscription = None
) -> ModelCategories:

    categories_list = list(CATEGORY_MAP.values())

    categories_out = ModelCategories(
        categories = categories_list
    )

    return categories_out
