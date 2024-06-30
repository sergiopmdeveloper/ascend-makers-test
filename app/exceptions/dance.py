from fastapi.exceptions import HTTPException


class DanceException(HTTPException):
    """
    Exception raised when something magical happens.
    """

    def __init__(self) -> None:
        """
        Initialize the exception.
        """

        super().__init__(
            status_code=500, detail="https://www.youtube.com/watch?v=hPr-Yc92qaY"
        )
