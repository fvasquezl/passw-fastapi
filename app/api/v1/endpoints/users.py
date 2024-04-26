from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.models import User
from app.api.schemas.user import UserCreate, User
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el correo electrónico ya existe
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Crear el usuario
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# @router.post("/login/access-token", response_model=Token)
# def login_access_token(
#     form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
# ):
#     # Obtener el usuario por correo electrónico
#     db_user = db.query(User).filter(User.email == form_data.username).first()
#     if db_user is None:
#         raise HTTPException(status_code=400, detail="Incorrect email or password")

#     # Verificar la contraseña
#     if not verify_password(form_data.password, db_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Incorrect email or password")

#     # Crear el token de acceso
#     access_token_expires = timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": db_user.email}, expires_delta=access_token_expires
#     )

#     return {"access_token": access_token, "token_type": "bearer"}


# @router.get("/me", response_model=UserRead)
# def read_users_me(current_user: str = Depends(get_current_user)):
#     # Aquí deberías obtener al usuario actual de la base de datos
#     # ...
#     return current_user


# @router.get("/", response_model=List[UserRead])
# def read_users(db: Session = Depends(get_db)):
#     users = db.query(User).all()
#     return users


# @router.get("/{user_id}", response_model=UserRead)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @router.patch("/me", response_model=UserRead)
# def update_user_me(
#     user: UserUpdate,
#     db: Session = Depends(get_db),
#     current_user: str = Depends(get_current_user),
# ):
#     # Obtener el usuario actual de la base de datos
#     # ...
#     # Actualizar los campos del usuario
#     # ...
#     return current_user


# @router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
# def delete_user_me(
#     db: Session = Depends(get_db), current_user: str = Depends(get_current_user)
# ):
#     # Obtener el usuario actual de la base de datos
#     # ...
#     # Eliminar el usuario
#     # ...
#     return
