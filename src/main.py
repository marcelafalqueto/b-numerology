from pathlib import Path
from fastapi import FastAPI
from .modules.routes.routes import router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()


app.include_router(router)


@app.get("/")
async def health():
    return {"status": "ok"}
