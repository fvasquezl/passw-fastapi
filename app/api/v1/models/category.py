from sqlalchemy import Column, Index, Integer, String
from sqlalchemy.orm import registry, Mapped, mapped_column

from app.core.database import Base

# mapper_registry = registry()


# @mapper_registry.mapped
class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True)
