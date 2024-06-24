from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

from datetime import date
from datetime import datetime

from typing import Annotated, Union, Optional

import random

app = FastAPI()

campaigns = []


class UserModel(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str


class CreateCampaignModel(BaseModel):
    start_date: date
    end_date: date
    budget: float
    type: str
    keywords: Optional[list[str]]
    urls: Optional[list[str]]


class CampaignListModel(BaseModel):
    campaigns: list[CreateCampaignModel]


def randomError() -> None:
    if random.randint(0, 9) == 0:
        raise HTTPException(status_code=500, detail="A random error has ocurred")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@app.post("/login")
def login(body: UserModel) -> LoginResponse:
    randomError()
    if body.username == "user" and body.password == "password":
        return LoginResponse(token="token")
    
    raise HTTPException(403, "Username and password are wrong")


@app.get("/campaign/list")
def list_campaigns(token: Annotated[Union[str, None], Header()] = None):
    if token != "token":
        return HTTPException(content="The token in invalid")
    randomError()
    return CampaignListModel(campaigns=campaigns)


@app.post("/campaign")
def create_campaign(
    body: CreateCampaignModel, token: Annotated[Union[str, None], Header()] = None
) -> CreateCampaignModel:
    if token != "token":
        return HTTPException(content="The token in invalid")
    randomError()
    if body.start_date >= datetime.today().date() and body.start_date <= body.end_date:
        if body.urls is not None and body.keywords is not None:
            raise HTTPException(
                400, detail="The fields urls and keywords cant be used at the same time"
            )
        if (body.type == "search" and body.keywords) or (
            body.type == "display" and body.urls
        ):
            campaigns.append(body)
            return body

        raise HTTPException(400, "invalid request")
