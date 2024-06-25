from datetime import date
from typing import Optional

from pydantic import UUID4, BaseModel


class CampaignInput(BaseModel):
    """
    Campaign input schema
    """

    start_date: date
    end_date: date
    budget: float
    type: str
    keywords: Optional[list[str]]
    urls: Optional[list[str]]

    def __init__(self, **data) -> None:
        """
        Convert empty lists to None
        in the keywords and urls fields.
        """

        if data.get("keywords") == []:
            data["keywords"] = None

        if data.get("urls") == []:
            data["urls"] = None

        super().__init__(**data)


class CampaignOutput(CampaignInput):
    """
    Campaign output schema
    """

    id: UUID4
