from pydantic import BaseModel
from typing import Optional, List

from .category import Category
from .tag import TagRead


class PostBase(BaseModel):
    title: str
    content: str
    category_id: int


class PostCreate(PostBase):
    tags: Optional[List[int]] = []


class PostUpdate(PostBase):
    title: Optional[str] = None
    content: Optional[str] = None
    category_id: Optional[int] = None
    tags: Optional[List[int]] = []


class PostRead(PostBase):
    id: int
    owner_id: int
    category: Category
    tags: List[TagRead] = []

    class Config:
        from_attributes = True
