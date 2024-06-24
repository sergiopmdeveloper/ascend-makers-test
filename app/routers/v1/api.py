from fastapi import APIRouter
from routers.v1.campaign import campaign_router

api_router = APIRouter(
    prefix="/api/v1",
    tags=["v1"],
)

api_router.include_router(campaign_router)
