from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.models import Category
from app.api.schemas.category import CategoryCreate, Category
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# @router.get("/", response_model=List[CategoryRead])
# def read_categories(db: Session = Depends(get_db)):
#     categories = db.query(Category).all()
#     return categories


# @router.get("/{category_id}", response_model=CategoryRead)
# def read_category(category_id: int, db: Session = Depends(get_db)):
#     db_category = db.query(Category).filter(Category.id == category_id).first()
#     if db_category is None:
#         raise HTTPException(status_code=404, detail="Category not found")
#     return db_category


# @router.patch("/{category_id}", response_model=CategoryRead)
# def update_category(
#     category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)
# ):
#     db_category = db.query(Category).filter(Category.id == category_id).first()
#     if db_category is None:
#         raise HTTPException(status_code=404, detail="Category not found")
#     db_category.name = category.name
#     db.commit()
#     db.refresh(db_category)
#     return db_category


# @router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_category(category_id: int, db: Session = Depends(get_db)):
#     db_category = db.query(Category).filter(Category.id == category_id).first()
#     if db_category is None:
#         raise HTTPException(status_code=404, detail="Category not found")
#     db.delete(db_category)
#     db.commit()
#     return
