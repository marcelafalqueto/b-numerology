# from ...i18n.provider import language_map
from typing import Literal, TypedDict, Optional

SupportedLanguageDTO = Literal["pt", "en"]  # Add the actual supported languages from language_map
SupportedLanguageVar: list[str] = ["pt", "en"] 
# NumerologyContent = type(next(iter(language_map.values())))


class NumerologicBlockDTO(TypedDict):
    number: int
    description: str


class NumerologicWithArrayNumberDTO(TypedDict):
    numbers: list[int]
    description: str


class LuckyNumbersDTO(TypedDict):
    harmonic: list[int]
    neutral: list[int]
    incompatible: list[int]
    description: str


class LifeCycleDTO(TypedDict):
    number: int
    duration: str
    from_to: str
    first_life_cycle_description: Optional[str]
    second_life_cycle_description: Optional[str]
    third_life_cycle_description: Optional[str]


class DecisiveMomentDTO(TypedDict):
    number: int
    description: str


class MapaNumerologicDTO(TypedDict):
    language: SupportedLanguageDTO
    motivation: NumerologicBlockDTO
    impression: NumerologicBlockDTO
    expression: NumerologicBlockDTO
    destiny: NumerologicBlockDTO
    mission: NumerologicBlockDTO
    psychic_number: NumerologicBlockDTO
    hidden_talent: NumerologicBlockDTO
    karmic_lesson: NumerologicWithArrayNumberDTO
    hidden_trends: NumerologicWithArrayNumberDTO
    lucky_numbers: LuckyNumbersDTO
    life_cycle: list[LifeCycleDTO]
    decisive_moment: list[DecisiveMomentDTO]
