import os

import requests
from dotenv import load_dotenv
from schemas.campaign import CampaignInput

load_dotenv()


def create_anam_campaign(data: CampaignInput) -> bool:
    """
    Create an ANAM campaign.

    Parameters
    ----------
    data : CampaignInput
        Campaign data.

    Returns
    -------
    bool
        True if the campaign was created
        successfully, False otherwise.
    """

    URL = os.getenv("ANAM_URL") + "/campaign"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "token": "token",
    }

    data = {
        "start_date": str(data.start_date),
        "end_date": str(data.end_date),
        "budget": data.budget,
        "type": data.type,
        "keywords": data.keywords,
        "urls": data.urls,
    }

    response = requests.post(URL, headers=headers, json=data)

    return response.ok
