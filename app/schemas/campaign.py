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


class CampaignOutput(CampaignInput):
    """
    Campaign output schema
    """

    id: UUID4
