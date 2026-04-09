# implementacao da logica de db_session, crud
from datetime import datetime

from sqlalchemy.orm import Session
from .models import MapModel
from ..schema.schema import MapSchema, UserInfoToGenerateMapSchema


class Repository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, map_generated: dict, user_info: UserInfoToGenerateMapSchema):
        data_dict = user_info.model_dump()
        data_dict["birth_date"] = data_dict["birth_date"]
        data_dict["map_generated"] = map_generated
        data_dict["created_at"] = datetime.now()

        create_map = MapModel(**data_dict)
        self.db_session.add(create_map)
        self.db_session.commit()

    def read(self, birth_date: str):
        result = self.db_session.query(MapModel).filter_by(birth_date=birth_date).all()

        return [
            {
                "id": r.id,
                "language": r.language,
                "name": r.name,
                "birth_date": r.birth_date,
                "map_generated": r.map_generated,
                "created_at": str(r.created_at),
            }
            for r in result
        ]
