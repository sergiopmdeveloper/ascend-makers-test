import os

import requests
from models.campaign import CampaignAnam
from schemas.campaign import CampaignAnamInput
from sqlalchemy.orm import Session


class CampaignAnamRepository:
    """
    Repository class for Campaign ANAM.
    """

    def __init__(self, session: Session) -> None:
        """
        Constructor for CampaignAnamRepository class.

        Parameters
        ----------
        session : Session
            Database session object.
        """

        self._session = session

    def create(self, campaign: CampaignAnamInput) -> bool:
        """
        Create a new ANAM campaign.

        Parameters
        ----------
        campaign : CampaignAnamInput
            Campaign data.

        Returns
        -------
        bool
            True if campaign is created
            successfully, False otherwise.
        """

        campaign_anam_instance = CampaignAnam(**campaign.dict())

        self._session.add(campaign_anam_instance)
        self._session.commit()
        self._session.refresh(campaign_anam_instance)

        URL = os.getenv("ANAM_URL") + "/campaign"

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "token": "token",
        }

        campaign_data = {
            "start_date": str(campaign.start_date),
            "end_date": str(campaign.end_date),
            "budget": campaign.budget,
            "type": campaign.type,
            "keywords": campaign.keywords,
            "urls": campaign.urls,
        }

        response = requests.post(URL, headers=headers, json=campaign_data)

        return response.ok

    def get_all(self) -> list[CampaignAnamInput]:
        """
        Get all ANAM campaigns.

        Returns
        -------
        list[CampaignAnamInput]
            List of ANAM campaigns.
        """

        URL = os.getenv("ANAM_URL") + "/campaign/list"

        headers = {
            "accept": "application/json",
            "token": "token",
        }

        response = requests.get(URL, headers=headers)
        data = response.json()["campaigns"]

        return [CampaignAnamInput(**campaign) for campaign in data]
