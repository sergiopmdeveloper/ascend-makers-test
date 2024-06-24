from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    """
    Redirects to the API documentation.
    """

    return RedirectResponse("/docs")
