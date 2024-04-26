# from __future__ import annotations
# from typing import List
# from sqlalchemy.orm import registry, Mapped, mapped_column, relationship
# from sqlalchemy import String, Integer
# from app.api.v1.models.post import Post
#
# from app.core.database import Base
#
#
# class Tag(Base):
#     __tablename__ = "tags"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String, unique=True, index=True)
#
#     # Relación
#     posts: Mapped[List[Post]] = relationship(
#         secondary="post_tags", back_populates="tags"
#     )