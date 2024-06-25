from datetime import date
from typing import Optional

from pydantic import UUID4, BaseModel


class CampaignOutput(BaseModel):
    """
    Campaign output schema
    """

    id: UUID4
    name: str
    created_in_anam: bool = False
    campaigns_anam: Optional[list] = None


class CampaignAnamInput(BaseModel):
    """
    Campaign ANAM input schema
    """

    campaign_id: Optional[UUID4] = None
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


class CampaignAnamFromPlatform(BaseModel):
    """
    Campaign ANAM from platform schema
    """

    start_date: date
    end_date: date
    budget: float
    type: str
    keywords: Optional[list[str]]
    urls: Optional[list[str]]
