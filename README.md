# Numerology API Backend

A simple Python backend for numerology-related API functionality.

## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the environment:
   ```bash
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   python3 -m pip install -e .
   ```

## Run Locally

Start the application with Uvicorn:
```bash
python -m uvicorn src.main:app --reload
```

## Test the API

Once the server is running, use a tool like `curl` or Postman to call the API endpoints.

Example using docs:
http://127.0.0.1:8000/docs

Go to the route `/mapa/{language}/{name}/{birth_date}` and try it out with:
language = en <!-- it accepts "pt" as well for portuguese -->
name = Your Complete Name <!-- It can have spaces between name -->
birth_date = 23091992 <!-- Do it in the format DDMMYYYY, without "/" between numbers -->

OR with curl: <!-- Remember to substitute information below -->

```curl -X 'POST' \
  'http://127.0.0.1:8000/mapa/en/marcela%20barreto%20falqueto/23091992' \
  -H 'accept: application/json' \
  -d ''
```

<!--

## Migrations

```bash
alembic revision --autogenerate -m "Add new column" 
alembic upgrade head
```

-->
