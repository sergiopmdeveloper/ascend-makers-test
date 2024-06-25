from datetime import datetime
from typing import Optional

from exceptions.campaign import InvalidCampaignData


def validate_campaign(
    start_date: str,
    end_date: str,
    type: str,
    keywords: Optional[list[str]] = None,
    urls: Optional[list[str]] = None,
    **kwargs,
):
    """
    Validate campaign data.

    Parameters
    ----------
    start_date : str
        Start date of the campaign.
    end_date : str
        End date of the campaign.
    type : str
        Type of the campaign.
    keywords : Optional[list[str]], optional
        Keywords for the campaign, by default None
    urls : Optional[list[str]], optional
        URLs for the campaign, by default None

    Raises
    ------
    InvalidCampaignData
        If one of the validations fails.
    """

    if start_date < datetime.now().date():
        raise InvalidCampaignData(error="Start date must be today or in the future.")

    if start_date > end_date:
        raise InvalidCampaignData(error="Start date must not be after end date.")

    if type not in ["search", "display"]:
        raise InvalidCampaignData(error="Campaign type must be 'search' or 'display'.")

    if type == "search" and (not keywords or urls):
        raise InvalidCampaignData(
            error="For 'search' campaigns, 'keywords' is required and 'urls' must be None."
        )
    elif type == "display" and (not urls or keywords):
        raise InvalidCampaignData(
            error="For 'display' campaigns, 'urls' is required and 'keywords' must be None."
        )
