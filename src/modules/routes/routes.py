from ..service.generate_map import NumerologyCalculatorService
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends
from ..db.repository import Repository
from ..db.base import get_db_session
from ..schema.schema import UserInfoToGenerateMapSchema

router = APIRouter()


@router.get("/mapa/{birth_date}", response_model=None)
def get_numerologic_map(
    birth_date: str,
    db_session: Session = Depends(get_db_session),
):
    repository = Repository(db_session)
    map_data = repository.read(birth_date=birth_date)
    return map_data


@router.post(
    "/mapa/{language}/{name}/{birth_date}", status_code=status.HTTP_201_CREATED
)
def numerologic_map(
    language: str,
    name: str,
    birth_date: str,
    db_session: Session = Depends(get_db_session),
):
    service = NumerologyCalculatorService()
    repository = Repository(db_session)
    map_generated = service.get_numerology_map(language, name, birth_date)
    user_info = UserInfoToGenerateMapSchema(
        language=language, name=name, birth_date=birth_date
    )
    repository.create(user_info=user_info, map_generated=map_generated)
    return map_generated


@router.post("/purchase")
def create_purchase():
    pass
