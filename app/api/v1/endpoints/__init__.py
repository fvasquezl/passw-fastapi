from fastapi import APIRouter

from .users import router as users_router
from .posts import router as posts_router
from .categories import router as categories_router
from .tags import router as tags_router

api_router = APIRouter()
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(posts_router, prefix="/posts", tags=["posts"])
api_router.include_router(categories_router, prefix="/categories", tags=["categories"])
api_router.include_router(tags_router, prefix="/tags", tags=["tags"])
