# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List
#
# from app.api.schemas.tag import TagCreate, TagRead, TagUpdate
# from app.api.v1.models.tag import Tag
# from app.core.database import get_db
#
# router = APIRouter()
#
#
# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=TagRead)
# def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
#     db_tag = Tag(**tag.dict())
#     db.add(db_tag)
#     db.commit()
#     db.refresh(db_tag)
#     return db_tag
#
#
# @router.get("/", response_model=List[TagRead])
# def read_tags(db: Session = Depends(get_db)):
#     tags = db.query(Tag).all()
#     return tags
#
#
# @router.get("/{tag_id}", response_model=TagRead)
# def read_tag(tag_id: int, db: Session = Depends(get_db)):
#     db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
#     if db_tag is None:
#         raise HTTPException(status_code=404, detail="Tag not found")
#     return db_tag
#
#
# @router.patch("/{tag_id}", response_model=TagRead)
# def update_tag(tag_id: int, tag: TagUpdate, db: Session = Depends(get_db)):
#     db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
#     if db_tag is None:
#         raise HTTPException(status_code=404, detail="Tag not found")
#     db_tag.name = tag.name
#     db.commit()
#     db.refresh(db_tag)
#     return db_tag
#
#
# @router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_tag(tag_id: int, db: Session = Depends(get_db)):
#     db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
#     if db_tag is None:
#         raise HTTPException(status_code=404, detail="Tag not found")
#     db.delete(db_tag)
#     db.commit()
#     return
