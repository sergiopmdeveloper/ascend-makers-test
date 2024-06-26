import pytest

from app.schemas.auth import Credentials


@pytest.fixture
def credentials() -> Credentials:
    """
    Fixture to return a Credentials object.
    """

    return Credentials(username="user", password="password")
