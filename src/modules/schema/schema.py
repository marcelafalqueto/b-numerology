from pydantic import BaseModel, Field, field_validator
from ..dto.dto import SupportedLanguageVar  # type: ignore
from typing import Any
import re


class UserInfoToGenerateMapSchema(BaseModel):
    language: str = Field(description="Language to generate the map")
    name: str = Field(description="Full name of the person")
    birth_date: str = Field(description="Birth date in DDMMYYYY format")

    @field_validator("language")
    def validate_language(cls, value: str):
        if value not in SupportedLanguageVar:
            raise ValueError(f"Invalid language. Must be one of {SupportedLanguageVar}")
        return value

    @field_validator("name")
    def validate_name(cls, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value

    @field_validator("birth_date")
    def validate_birth_date(cls, value: str):
        if not re.match(r"^\d{8}$", value):
            raise ValueError("Birth date must be in DDMMYYYY format")
        return value


class MapSchema(BaseModel):
    id: int = Field(description="Unique identifier for the map")
    name: str = Field(description="Full name of the person")
    birth_date: str = Field(description="Birth date in DDMMYYYY format")
    map_generated: dict[str, Any] = Field(description="Generated numerology map")
    created_at: str = Field(description="Timestamp when the map was created")
    language: str = Field(description="Language to generate the map")

    @field_validator("language")
    def validate_language(cls, value: str):
        if value not in SupportedLanguageVar:
            raise ValueError(f"Invalid language. Must be one of {SupportedLanguageVar}")
        return value

    @field_validator("name")
    def validate_name(cls, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value

    @field_validator("birth_date")
    def validate_birth_date(cls, value: str):
        if not re.match(r"^\d{8}$", value):
            raise ValueError("Birth date must be in DDMMYYYY format")
        return value
