from fastapi.exceptions import HTTPException


class AuthException(HTTPException):
    """
    Exception raised when authentication fails.
    """

    def __init__(self) -> None:
        """
        Initialize the exception.
        """

        super().__init__(status_code=401, detail="Unauthorized.")
