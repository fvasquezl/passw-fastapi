# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session

# from app.api.v1.models import Post, Category, Tag
# from app.api.schemas.post import PostCreate, Post
# from app.core.database import get_db

# router = APIRouter()


# @router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
# def create_post(
#     post: PostCreate, db: Session = Depends(get_db)
# ):
#     # Verificar si la categoría existe
#     db_category = db.query(Category).filter(Category.id == post.category_id).first()
#     if db_category is None:
#         raise HTTPException(status_code=404, detail="Category not found")

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

#     # Crear el post
#     db_post = Post(**post.model_dump(), owner_id=current_user, tags=tags)
#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)
#     return db_post


# @router.get("/", response_model=List[PostRead])
# def read_posts(db: Session = Depends(get_db)):
#     posts = db.query(Post).all()
#     return posts


# @router.get("/{post_id}", response_model=PostRead)
# def read_post(post_id: int, db: Session = Depends(get_db)):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return db_post


# @router.patch("/{post_id}", response_model=PostRead)
# def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")

#     # Actualizar los campos del post
#     for key, value in post.model_dump(exclude_unset=True).items():
#         setattr(db_post, key, value)

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

#     db.commit()
#     db.refresh(db_post)
#     return db_post


# @router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(post_id: int, db: Session = Depends(get_db)):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     db.delete(db_post)
#     db.commit()
#     return


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.models import Post, Category, Tag
from app.api.schemas.post import PostCreate, Post
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    # Verificar que la categoría existe
    category = db.query(Category).filter(Category.id == post.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    # Crear tags que no existan y obtener todos los tags
    tags = []
    for tag_id in post.tag_ids:
        tag = db.query(Tag).filter(Tag.id == tag_id).first()
        if not tag:
            tag = Tag(name=tag_id)
            db.add(tag)
            db.flush()
        tags.append(tag)

    # Crear el post
    db_post = Post(**post.dict(), category=category, tags=tags)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@router.get("/", response_model=list[Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = db.query(Post).offset(skip).limit(limit).all()
    return posts


@router.get("/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.put("/{post_id}", response_model=Post)
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    # Actualizar categoría y tags (similar a la creación)
    # ...

    # Actualizar el post
    for key, value in post.dict().items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(db_post)
    db.commit()
    return
