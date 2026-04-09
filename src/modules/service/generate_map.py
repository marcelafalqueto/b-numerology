import re
import unicodedata
from typing import Any, Dict, List

from ...i18n.provider import NumerologyContentProvider


class NumerologyCalculatorService:
    def __init__(self) -> None:
        self.base_table: Dict[str, int] = {
            "A": 1,
            "I": 1,
            "Q": 1,
            "J": 1,
            "Y": 1,
            "B": 2,
            "K": 2,
            "R": 2,
            "C": 3,
            "G": 3,
            "L": 3,
            "S": 3,
            "D": 4,
            "M": 4,
            "T": 4,
            "E": 5,
            "H": 5,
            "N": 5,
            "U": 6,
            "V": 6,
            "W": 6,
            "X": 6,
            "Ç": 6,
            "O": 7,
            "Z": 7,
            "F": 8,
            "P": 8,
        }

        self.lucky_numbers_base: Dict[int, Dict[str, List[int]]] = {
            1: {"harmonic": [2, 4, 9], "neutral": [1, 5, 6, 8], "incompatible": [3, 7]},
            2: {
                "harmonic": [1, 2, 3, 4, 5, 6, 7, 8, 9],
                "neutral": [],
                "incompatible": [],
            },
            3: {"harmonic": [2, 3, 6, 8, 9], "neutral": [4, 7], "incompatible": [1, 5]},
            4: {
                "harmonic": [1, 2, 6, 7, 8],
                "neutral": [3, 5, 9],
                "incompatible": [4, 8],
            },
            5: {"harmonic": [2, 5, 6, 7, 9], "neutral": [1, 4], "incompatible": [3, 8]},
            6: {"harmonic": [2, 3, 4, 5, 6, 9], "neutral": [1], "incompatible": [7, 8]},
            7: {"harmonic": [2, 4, 5, 7], "neutral": [3, 9], "incompatible": [1, 6, 8]},
            8: {"harmonic": [2, 3, 9], "neutral": [1, 6], "incompatible": [4, 5, 7, 8]},
            9: {
                "harmonic": [1, 2, 3, 5, 6, 8, 9],
                "neutral": [4, 7],
                "incompatible": [],
            },
        }

    def normalize_text(self, text: str) -> str:
        return unicodedata.normalize("NFD", text.upper())

    def apply_modifier(self, value: int, symbol: str | None) -> int:
        if not symbol:
            return value
        if symbol == "\u0302":
            return value + 7
        if symbol == "\u0303":
            return value + 3
        if symbol in ("\u0308", "\u0300"):
            return value * 2
        if symbol == "\u0301":
            return value + 2
        return value

    def extract_vowels_regex(self, text: str) -> str:
        normalized = self.normalize_text(text)
        matches = re.findall(r"[AEIOU][\u0300-\u036f]?", normalized)
        return "" if not matches else "".join(matches)

    def extract_consonants_regex(self, text: str) -> str:
        normalized = self.normalize_text(text)
        matches = re.findall(r"[BCÇDFGHJKLMNPQRSTVWXYZ][\u0300-\u036f]?", normalized)
        return "" if not matches else "".join(matches)

    def reduce_simple_number(self, num: int) -> int:
        while num > 9:
            num = sum(int(d) for d in str(num))
        return num

    def reduce_number_check_master_numbers(self, *numbers: int) -> int:
        total = 0
        for n in numbers:
            total += sum(int(d) for d in str(n))
        while total > 9:
            if total in (11, 22):
                return total
            total = sum(int(d) for d in str(total))
        return total

    def calculate_vowels_per_word(self, text: str) -> List[int]:
        words = text.strip().split() if text.strip() else []
        return [
            self.calculate_letter_value(self.extract_vowels_regex(w)) for w in words
        ]

    def calculate_complete_name_value_per_word(self, text: str) -> List[int]:
        words = text.strip().split() if text.strip() else []
        return [self.calculate_letter_value(w) for w in words]

    def reduce_check_if_2_or_4_vowel(self, name: str) -> int:
        vowel_values = self.calculate_vowels_per_word(name)
        reduced_values = [self.reduce_simple_number(v) for v in vowel_values]
        s = sum(reduced_values)
        return self.reduce_number_check_master_numbers(s)

    def reduce_check_if_2_or_4_complete_name(self, name: str) -> int:
        word_values = self.calculate_complete_name_value_per_word(name)
        reduced_values = [self.reduce_simple_number(v) for v in word_values]
        s = sum(reduced_values)
        return self.reduce_number_check_master_numbers(s)

    def birth_date_to_digits(self, birth_date: str) -> int:
        digits = birth_date.replace("0", "")
        return int(digits) if digits else 0

    def birth_day_to_digits(self, birth_date: str) -> int:
        d = birth_date[0:2]
        # digits = d.replace("0", "")
        return int(d) if d else 0

    def birth_month_to_digits(self, birth_date: str) -> int:
        m = birth_date[2:4]
        # digits = m.replace("0", "")
        return int(m) if m else 0

    def birth_year_to_digits(self, birth_date: str) -> int:
        y = birth_date[4:8]
        # digits = y.replace("0", "")
        return int(y) if y else 0

    def get_description(self, section: Dict[str, str], number: int) -> str:
        return section.get(str(number), "")

    def calculate_letter_value(self, text: str) -> int:
        chars = self.normalize_text(text)
        total = 0
        i = 0
        while i < len(chars):
            ch = chars[i]
            # skip combining marks
            if unicodedata.category(ch) == "Mn":
                i += 1
                continue
            value = self.base_table.get(ch)
            if value is None:
                i += 1
                continue
            modifier = None
            if i + 1 < len(chars) and unicodedata.category(chars[i + 1]) == "Mn":
                modifier = chars[i + 1]
            total += self.apply_modifier(value, modifier)
            i += 1
        return total

    def calculate_motivation(self, name: str) -> int:
        vowels = self.extract_vowels_regex(name)
        total = self.calculate_letter_value(vowels)
        total = self.reduce_number_check_master_numbers(total)
        if total in (2, 4):
            total = self.reduce_check_if_2_or_4_vowel(name)
        return total

    def calculate_impression(self, name: str) -> int:
        consonants = self.extract_consonants_regex(name)
        total = self.calculate_letter_value(consonants)
        return self.reduce_simple_number(total)

    def calculate_expression(self, name: str) -> int:
        vowels = self.extract_vowels_regex(name)
        consonants = self.extract_consonants_regex(name)
        total = self.calculate_letter_value(consonants) + self.calculate_letter_value(
            vowels
        )
        total = self.reduce_simple_number(total)
        if total in (2, 4):
            total = self.reduce_check_if_2_or_4_complete_name(name)
        return total

    def calculate_destiny(self, birth_date: str) -> int:
        transformed = self.birth_date_to_digits(birth_date)
        return self.reduce_number_check_master_numbers(transformed)

    def calculate_mission(self, name: str, birth_date: str) -> int:
        expression = self.calculate_expression(name)
        destiny = self.calculate_destiny(birth_date)
        total = expression + destiny
        return self.reduce_number_check_master_numbers(total)

    def calculate_psychic(self, birth_date: str) -> int:
        b_day = self.birth_day_to_digits(birth_date)
        return self.reduce_simple_number(b_day)

    def calculate_life_cycle(self, birth_date: str) -> List[Dict[str, Any]]:
        b_day = self.birth_day_to_digits(birth_date)
        m_month = self.birth_month_to_digits(birth_date)
        y_year = self.birth_year_to_digits(birth_date)
        destiny = self.calculate_destiny(birth_date)

        first_life_cycle_number = self.reduce_number_check_master_numbers(m_month)
        second_life_cycle_number = self.reduce_number_check_master_numbers(b_day)
        third_life_cycle_number = self.reduce_number_check_master_numbers(y_year)
        first_life_cycle_duration = 37 - destiny
        second_life_cycle_duration = y_year + first_life_cycle_duration + 27

        return [
            {
                "number": first_life_cycle_number,
                "duration": str(first_life_cycle_duration),
                "from_to": f"{y_year} - {y_year + first_life_cycle_duration}",
            },
            {
                "number": second_life_cycle_number,
                "duration": "27",
                "from_to": f"{y_year + first_life_cycle_duration + 1} - {second_life_cycle_duration}",
            },
            {
                "number": third_life_cycle_number,
                "duration": "...",
                "from_to": f"{second_life_cycle_duration + 1} - ...",
            },
        ]

    def calculate_decisive_moment(self, birth_date: str) -> List[Dict[str, Any]]:
        b_day = self.birth_day_to_digits(birth_date)
        m_month = self.birth_month_to_digits(birth_date)
        y_year = self.birth_year_to_digits(birth_date)
        destiny = self.calculate_destiny(birth_date)
        energy1 = self.reduce_number_check_master_numbers(b_day, m_month)
        energy2 = self.reduce_number_check_master_numbers(b_day, y_year)
        energy3 = self.reduce_number_check_master_numbers(energy1, energy2)
        energy4 = self.reduce_number_check_master_numbers(m_month, y_year)
        first_life_cycle_duration = 37 - destiny + y_year
        second_life_cycle_duration = first_life_cycle_duration + 9
        third_life_cycle_duration = second_life_cycle_duration + 9

        return [
            {"number": energy1, "duration": f"{y_year} - {first_life_cycle_duration}"},
            {
                "number": energy2,
                "duration": f"{first_life_cycle_duration} - {second_life_cycle_duration}",
            },
            {
                "number": energy3,
                "duration": f"{second_life_cycle_duration} - {third_life_cycle_duration}",
            },
            {"number": energy4, "duration": f"{third_life_cycle_duration} - ..."},
        ]

    def calculate_karmic_lesson(self, name: str) -> List[int]:
        normalized = self.normalize_text(name)
        present_numbers = set() # pyright: ignore[reportUnknownVariableType]
        for ch in normalized:
            val = self.base_table.get(ch)
            if val is not None:
                present_numbers.add(val) # pyright: ignore[reportUnknownMemberType]
        karmic = [i for i in range(1, 10) if i not in present_numbers]
        return karmic

    def calculate_hidden_trends(self, name: str) -> List[int]:
        normalized = self.normalize_text(name)
        freq: Dict[int, int] = {}
        for ch in normalized:
            val = self.base_table.get(ch)
            if val is not None:
                freq[val] = freq.get(val, 0) + 1
        hidden = [v for v, count in freq.items() if count > 3]
        return sorted(hidden)

    def calculate_hidden_talent(self, name: str) -> int:
        expression = self.calculate_expression(name)
        motivation = self.calculate_motivation(name)
        total = self.reduce_simple_number(expression + motivation)
        return total

    def calculate_lucky_numbers(self, birth_date: str) -> Dict[str, List[int]]:
        b_day = self.birth_day_to_digits(birth_date)
        total = self.reduce_simple_number(b_day)
        return self.lucky_numbers_base.get(
            total, {"harmonic": [], "neutral": [], "incompatible": []}
        )

    def get_numerology_map(
        self, language: str, name: str, birth_date: str
    ) -> Dict[str, Any]:
        language_content = NumerologyContentProvider().get_content(language)
        life_cycle_keys = list(language_content["life_cycle"].keys())

        motivation_number = self.calculate_motivation(name)
        impression_number = self.calculate_impression(name)
        expression_number = self.calculate_expression(name)
        destiny_number = self.calculate_destiny(birth_date)
        mission_number = self.calculate_mission(name, birth_date)
        psychic_number = self.calculate_psychic(birth_date)
        life_cycle_number = self.calculate_life_cycle(birth_date)
        decisive_moment_number = self.calculate_decisive_moment(birth_date)
        karmic_lesson_number = self.calculate_karmic_lesson(name)
        hidden_trends_number = self.calculate_hidden_trends(name)
        hidden_talent_number = self.calculate_hidden_talent(name)

        motivation_language = language_content.get("motivation", {})
        impression_language = language_content.get("impression", {})
        expression_language = language_content.get("expression", {})
        destiny_language = language_content.get("destiny", {})
        mission_language = language_content.get("mission", {})
        psychic_language = language_content.get("psychic_number", {})
        life_cycle_language = language_content.get("life_cycle", {})
        decisive_moment_language = language_content.get("decisive_moment", {})
        karmic_lesson_language = language_content.get("karmic_lesson", {})
        hidden_trends_language = language_content.get("hidden_trends", {})
        hidden_talent_language = language_content.get("hidden_talent", {})

        def desc(section: Dict[str, str], num: int) -> str:
            return section.get(str(num), "")

        life_cycle_descriptions = [
            desc(life_cycle_language.get(k, {}), cycle["number"])
            for k, cycle in zip(life_cycle_keys, life_cycle_number)
        ]

        karmic_lesson_description = (
            ", ".join(desc(karmic_lesson_language, n) for n in karmic_lesson_number)
            if karmic_lesson_number
            else language_content.get("karmic_lesson", {}).get("no_karmic_lesson", "")
        )

        hidden_trends_description = (
            ", ".join(desc(hidden_trends_language, n) for n in hidden_trends_number)
            if hidden_trends_number
            else language_content.get("hidden_trends", {}).get("no_hidden_trends", "")
        )

        # build result
        return {
            "motivation": {
                "number": motivation_number,
                "description": desc(motivation_language, motivation_number),
            },
            "impression": {
                "number": impression_number,
                "description": desc(impression_language, impression_number),
            },
            "expression": {
                "number": expression_number,
                "description": desc(expression_language, expression_number),
            },
            "destiny": {
                "number": destiny_number,
                "description": desc(destiny_language, destiny_number),
            },
            "mission": {
                "number": mission_number,
                "description": desc(mission_language, mission_number),
            },
            "psychic_number": {
                "number": psychic_number,
                "description": desc(psychic_language, psychic_number),
            },
            "karmic_lesson": {
                "numbers": karmic_lesson_number,
                "description": karmic_lesson_description,
            },
            "hidden_trends": {
                "numbers": hidden_trends_number,
                "description": hidden_trends_description,
            },
            "hidden_talent": {
                "number": hidden_talent_number,
                "description": desc(hidden_talent_language, hidden_talent_number),
            },
            "life_cycle": [
                {
                    "number": life_cycle_number[i]["number"],
                    "duration": life_cycle_number[i]["duration"],
                    "from_to": life_cycle_number[i]["from_to"],
                    "description": life_cycle_descriptions[i],
                }
                for i in range(len(life_cycle_number))
            ],
            "decisive_moment": [
                {
                    "number": m["number"],
                    "duration": m["duration"],
                    "description": desc(decisive_moment_language, m["number"]),
                }
                for m in decisive_moment_number
            ],
        }
