import json
from pathlib import Path

# Resolve the numerology i18n folder relative to this file
BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "pt.json", encoding="utf-8") as f:
    pt = json.load(f)

with open(BASE_DIR / "en.json", encoding="utf-8") as f:
    en = json.load(f)

language_map = {
    "pt": pt,
    "en": en,
}

supported_languages = list(language_map.keys())


class NumerologyContentProvider:
    def get_content(self, language: str):
        try:
            return language_map[language]
        except KeyError as exc:
            raise ValueError(f"Unsupported language: {language}") from exc
