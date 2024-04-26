from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
