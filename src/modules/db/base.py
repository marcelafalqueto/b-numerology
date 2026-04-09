from sqlalchemy.orm import declarative_base
from .conection import Session

BaseModel = declarative_base()


def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
