from __future__ import annotations
from typing import List
from sqlalchemy.orm import registry, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Boolean

# from app.api.v1.models.post import Post


from app.core.database import Base

# mapper_registry = registry()


# @mapper_registry.mapped
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relación
    # posts: Mapped[List[Post]] = relationship(back_populates="owner")
