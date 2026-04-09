validationMessages: dict[str, dict[str, dict[str, str]]] = {
    "pt": {
        "language": {
            "enum": "Idioma não suportado",
        },
        "name": {
            "required": "O nome é obrigatório",
            "invalid": "O nome deve conter apenas letras e espaços e/ou acentos",
            "min": "O nome deve ter pelo menos 3 caracteres",
        },
        "birth_date": {
            "length": "A data de nascimento deve ter 8 caracteres",
            "regex": "A data de nascimento deve conter apenas números",
            "refine": "Data de nascimento inválida",
        },
        "couponCode": {},
    },
    "en": {
        "language": {
            "enum": "Unsupported language",
        },
        "name": {
            "required": "Name is required",
            "invalid": "Name must contain only letters and spaces",
            "min": "Name must be at least 3 characters long",
        },
        "birth_date": {
            "length": "Birth date must be 8 characters long",
            "regex": "Birth date must contain only numbers",
            "refine": "Invalid birth date",
        },
        "couponCode": {},
    },
}
