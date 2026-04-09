# Numerology API Backend

## Overview

This is a study project created to practice building a complete backend application end-to-end. The project calculates numerology maps and readings based on personal information (name and birth date), stores the data in a relational database, and exposes results through a RESTful API.

The application processes user input through a numerology calculation service, persists results using SQLAlchemy ORM, and provides international support for multiple languages.

The project still in progress...

## Project Goal

The main goal is learning and practice, especially:

- Building a numerology calculator service with complex business logic
- Saving calculated data to a relational database (PostgreSQL)
- Using SQLAlchemy as the ORM layer with Alembic for migrations
- Creating a RESTful API with FastAPI
- Validating request and response schemas with Pydantic
- Implementing internationalization (i18n) for multiple languages
- Structuring backend services with clean architecture patterns

## How It Works

### 1. Numerology Calculation
The `NumerologyCalculatorService` receives a person's complete name and birth date, then:
- Converts letters to numbers according to the numerology base table
- Calculates various numerological indicators (life path, destiny number, etc.)
- Determines lucky numbers, harmonic relationships, and personal insights

### 2. Data Storage
The Alembic migration system manages database schema versions, and SQLAlchemy models persist:
- User information and calculation inputs
- Generated numerology maps and readings
- Indexed data for efficient retrieval

### 3. Internationalization (i18n)
Supporting multiple languages (English and Portuguese):
- Localized response messages and content
- Language-specific validation messages
- Dynamic content provider based on user selection

### 4. Serving Data with FastAPI
The FastAPI application provides endpoints to:
- Calculate and retrieve numerology maps
- Validate incoming requests with Pydantic schemas
- Return structured JSON responses with full API documentation

### 5. Schema Validation with Pydantic
Request and response validation ensures:
- Data integrity for user inputs (name, birth date)
- Type safety across the API
- Clear error messages for invalid requests

## Main Tech Stack

- **Python 3.12+** - Core language
- **FastAPI** - Web framework for building the REST API
- **SQLAlchemy 2.0** - ORM for database operations
- **PostgreSQL** - Relational database
- **Alembic** - Database migration tool
- **Pydantic** - Data validation and schema definition
- **Uvicorn** - ASGI server for running the application
- **python-decouple** - Environment configuration management

## Setup

### Prerequisites
- Python 3.12 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd b-numerology
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -e .
   ```

5. Configure environment variables:
   ```bash
   cp .env.example .env  # Create your .env file with database credentials
   ```

6. Run database migrations:
   ```bash
   alembic upgrade head
   ```

## Run Locally

Start the application with Uvicorn:

```bash
python -m uvicorn src.main:app --reload
```

The server will start at `http://127.0.0.1:8000`

## API Documentation

Once the server is running, access the interactive API documentation:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Test the API

### Using Swagger UI (Recommended)
Navigate to http://127.0.0.1:8000/docs and try the endpoints directly from the browser.

### Using cURL

Replace the values below with your own information:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/mapa/23091992' \
  -H 'accept: application/json'
```

### Parameters

- `birth_date` - Birth date in format **DDMMYYYY** (without slashes)
  - Example: `23091992` for September 23, 1992

### Example Response

```json
{
  "birth_date": "23091992",
  "life_path_number": 7,
  "destiny_number": 9,
  "lucky_numbers": [1, 4, 7],
  "personality_insights": {
    "strengths": ["Analytical", "Spiritual", "Intuitive"],
    "challenges": ["Overthinking", "Social Withdrawal"]
  }
}
```

## Database Migrations

### Creating a New Migration

```bash
alembic revision --autogenerate -m "Description of your changes"
```

### Applying Migrations

```bash
alembic upgrade head
```

### Downgrading Migrations

```bash
alembic downgrade -1
```

## Project Structure

```
src/
├── main.py                    # FastAPI app initialization
├── modules/
│   ├── service/              # Business logic
│   │   └── generate_map.py   # Numerology calculation service
│   ├── db/                   # Database layer
│   │   ├── models.py         # SQLAlchemy models
│   │   ├── repository.py     # Data access layer
│   │   └── conection.py      # Database connection setup
│   ├── routes/               # API endpoints
│   │   └── routes.py         # Route definitions
│   ├── schema/               # Pydantic schemas
│   │   └── schema.py         # Request/response validation
│   ├── dto/                  # Data transfer objects
│   │   └── dto.py            # DTO definitions
│   ├── middlewares/          # Middleware components
│   │   ├── error_handler.py  # Global error handling
│   │   └── validate_schema.py # Schema validation middleware
│   └── i18n/                 # Internationalization
│       ├── en.json           # English translations
│       ├── pt.json           # Portuguese translations
│       └── provider.py       # i18n content provider
└── alembic/                  # Database migrations
    └── versions/             # Migration files
```

## Environment Variables

Create a `.env` file in the project root with:

```
DATABASE_URL=postgresql://user:password@localhost/numerology_db
# or for SQLite:
# DATABASE_URL=sqlite:///./numerology.db

DEBUG=True
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Create a migration if modifying the database schema
4. Test your changes locally
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
