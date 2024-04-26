from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings


# Crear el motor de la base de datos
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Crear una base declarativa
class Base(DeclarativeBase):
    pass


Base.metadata.create_all(bind=engine)


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
