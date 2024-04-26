from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

# Create the engine of database
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
# Create a local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Create a declarative database
class Base(DeclarativeBase):
    pass


class NotFoundError(Exception):
    pass


Base.metadata.create_all(bind=engine)


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
