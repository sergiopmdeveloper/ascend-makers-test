import os

import requests
from exceptions.auth import AuthException
from exceptions.dance import DanceException
from schemas.auth import Credentials


def generate_token(credentials: Credentials) -> str:
    """
    Generate token

    Parameters
    ----------
    credentials : Credentials
        User credentials.

    Returns
    -------
    str
        Token.
    """

    URL = os.getenv("ANAM_URL") + "/login"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    data = {
        "username": credentials.username,
        "password": credentials.password,
    }

    response = requests.post(URL, headers=headers, json=data)

    if response.status_code == 500:
        raise DanceException()
    if response.status_code == 403:
        raise AuthException()

    return response.json()["token"]
