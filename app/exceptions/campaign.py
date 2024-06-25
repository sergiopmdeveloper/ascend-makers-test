from fastapi.exceptions import HTTPException


class InvalidCampaignData(HTTPException):
    """
    Exception raised when the campaign data is invalid.
    """

    def __init__(self, error: str) -> None:
        """
        Initialize the exception.

        Parameters
        ----------
        error : str
            Error message.
        """

        super().__init__(status_code=400, detail=error)
