from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@app.get("/hello_world")
def hello_world():
    return "Hello World"
