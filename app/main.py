from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from utils.init_db import create_tables

app = FastAPI()


@app.on_event("startup")
def on_startup() -> None:
    """
    Initializes the database tables
    when the application starts.
    """

    create_tables()


@app.get("/", include_in_schema=False)
async def root():
    """
    Redirects to the API documentation.
    """

    return RedirectResponse("/docs")
