from unittest.mock import patch

import pytest
from fastapi.exceptions import HTTPException
from pytest import MonkeyPatch

from app.schemas.auth import Credentials
from app.utils.auth import generate_token


def test_generate_token_anam_url_and_headers(credentials: Credentials):
    """
    Test that the generate_token function calls
    the correct URL with the correct headers.
    """

    monkeypatch = MonkeyPatch()
    monkeypatch.setenv("ANAM_URL", "url")

    with patch("requests.post") as mock_post:
        generate_token(credentials)

        mock_post.assert_called_with(
            "url/login",
            headers={"accept": "application/json", "Content-Type": "application/json"},
            json={"username": "user", "password": "password"},
        )


def test_generate_token_raises_dance_http_exception(credentials: Credentials):
    """
    Test that the generate_token function raises a HTTPException
    with status code 500 and detail "https://www.youtube.com/watch?v=uUxChessSEY"
    when the response status code is 500.
    """

    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 500

        with pytest.raises(HTTPException) as exc_info:
            generate_token(credentials)

        assert exc_info.value.status_code == 500
        assert exc_info.value.detail == "https://www.youtube.com/watch?v=uUxChessSEY"


def test_generate_token_raises_auth_http_exception(credentials: Credentials):
    """
    Test that the generate_token function raises a HTTPException
    with status code 401 and detail "Unauthorized."
    when the response status code is 403.
    """

    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 403

        with pytest.raises(HTTPException) as exc_info:
            generate_token(credentials)

        assert exc_info.value.status_code == 401
        assert exc_info.value.detail == "Unauthorized."


def test_generate_token_returns_token(credentials: Credentials):
    """
    Test that the generate_token function
    returns the token from the response JSON.
    """

    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = {"token": "token"}

        token = generate_token(credentials)

        assert token == "token"
