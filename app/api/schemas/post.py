from pydantic import BaseModel
from .category import Category
from .tag import Tag


class PostBase(BaseModel):
    title: str
    content: str
    category_id: int
    tag_ids: list[int] = []


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    user_id: int
    category: (
        "Category"  # Importar el esquema Category para evitar importaciones circulares
    )
    tags: list["Tag"] = (
        []
    )  # Importar el esquema Tag para evitar importaciones circulares

    class Config:
        orm_mode = True
