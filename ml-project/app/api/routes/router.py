

from fastapi import APIRouter

from app.api.routes import heartbeat, prediction, categories

api_router = APIRouter()
api_router.include_router(
    heartbeat.router, 
    tags=["health"], 
    prefix="/health"
    )
api_router.include_router(
    prediction.router, 
    tags=["prediction"], 
    prefix="/model"
    )
api_router.include_router(
    categories.router, 
    tags=["categories"], 
    prefix="/model"
    )
