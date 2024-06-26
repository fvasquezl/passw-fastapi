# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List
#
# from app.api.schemas.post import PostCreate, PostRead, PostUpdate
# from app.api.v1.models.post import Post
# from app.api.v1.models.category import Category
# from app.api.v1.models.tag import Tag
# from app.core.database import get_db
# from app.core.security import get_current_user
#
# router = APIRouter()
#
#
# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostRead)
# def create_post(
#     post: PostCreate,
#     db: Session = Depends(get_db),
#     current_user: str = Depends(get_current_user),
# ):
#     # Verificar si la categoría existe
#     db_category = db.query(Category).filter(Category.id == post.category_id).first()
#     if db_category is None:
#         raise HTTPException(status_code=404, detail="Category not found")
#
#     # Obtener o crear los tags
#     tags = []
#     for tag_id in post.tags:
#         db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
#         if db_tag is None:
#             db_tag = Tag(
#                 name=tag_id
#             )  # Asumimos que el tag_id es el nombre del tag si no existe
#             db.add(db_tag)
#             db.commit()
#             db.refresh(db_tag)
#         tags.append(db_tag)
#
#     # Crear el post
#     db_post = Post(**post.model_dump(), owner_id=current_user, tags=tags)
#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)
#     return db_post
#
#
# @router.get("/", response_model=List[PostRead])
# def read_posts(db: Session = Depends(get_db)):
#     posts = db.query(Post).all()
#     return posts
#
#
# @router.get("/{post_id}", response_model=PostRead)
# def read_post(post_id: int, db: Session = Depends(get_db)):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return db_post
#
#
# @router.patch("/{post_id}", response_model=PostRead)
# def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#
#     # Actualizar los campos del post
#     for key, value in post.model_dump(exclude_unset=True).items():
#         setattr(db_post, key, value)
#
#     # Obtener o crear los tags
#     if post.tags:
#         tags = []
#         for tag_id in post.tags:
#             db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
#             if db_tag is None:
#                 db_tag = Tag(
#                     name=tag_id
#                 )  # Asumimos que el tag_id es el nombre del tag si no existe
#                 db.add(db_tag)
#                 db.commit()
#                 db.refresh(db_tag)
#             tags.append(db_tag)
#         db_post.tags = tags
#
#     db.commit()
#     db.refresh(db_post)
#     return db_post
#
#
# @router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(post_id: int, db: Session = Depends(get_db)):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     db.delete(db_post)
#     db.commit()
#     return
