from datetime import datetime

from .base import BaseModel
from sqlalchemy import JSON, Column, Integer, String, DateTime


class MapModel(BaseModel):
    __tablename__ = "maps"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    language = Column(String, nullable=False)
    name = Column(String, nullable=False)
    birth_date = Column(String, nullable=False)
    map_generated = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
