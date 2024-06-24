from datetime import date
from typing import Optional

from pydantic import BaseModel


class CampaignAscendInput(BaseModel):
    """
    Campaign Ascend Input Schema
    """

    start_date: date
    end_date: date
    budget: float
    type: str
    keywords: Optional[list[str]]
    urls: Optional[list[str]]
