from fastapi import APIRouter

from app.api.v1.endpoints import users, posts, categories, tags

api_router = APIRouter()
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
# api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
