# from __future__ import annotations
# from datetime import datetime
# from typing import List, TYPE_CHECKING
# from sqlalchemy import Integer, String, ForeignKey, DateTime
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# if TYPE_CHECKING:
#     from app.api.v1.models.user import User
#     # from app.api.v1.models.category import Category
#     from app.api.v1.models.tag import Tag
# else:
#     User = "User"
#     # Category = "Category"
#     Tag = "Tag"
#
# from app.core.database import Base
#
#
# class Post(Base):
#     __tablename__ = "posts"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(String, index=True)
#     content: Mapped[str] = mapped_column(String)
#     owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
#     category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), server_default=func.now()
#     )
#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), onupdate=func.now()
#     )
#
#     # Relaciones
#     owner: Mapped[User] = relationship(back_populates="posts")
#     # category: Mapped[Category] = relationship(back_populates="posts")
#     tags: Mapped[List[Tag]] = relationship(
#         secondary="post_tags", back_populates="posts"
#     )
