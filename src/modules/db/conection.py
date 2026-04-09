from pathlib import Path

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


PROJECT_ROOT = Path(__file__).resolve().parents[2] 
DATABASE_URL = config("DATABASE_URL", ) # pyright: ignore[reportUnknownVariableType]

engine = create_engine(DATABASE_URL, pool_pre_ping=True, future=True) # pyright: ignore[reportUnknownVariableType, reportArgumentType, reportCallIssue]
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True) # type: ignore

Session = SessionLocal
