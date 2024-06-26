from pydantic import BaseModel


class Credentials(BaseModel):
    """
    Credentials schema
    """

    username: str
    password: str
