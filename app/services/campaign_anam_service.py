from repositories.campaign_anam_repository import CampaignAnamRepository
from schemas.campaign import CampaignAnamInput
from sqlalchemy.orm import Session


class CampaignAnamService:
    """
    Service class for Campaign Anam.
    """

    def __init__(self, session: Session) -> None:
        """
        Constructor for CampaignAnamService class.

        Parameters
        ----------
        session : Session
            Database session object.
        """

        self._repository = CampaignAnamRepository(session)

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

        return self._repository.create(campaign)

    def get_all(self) -> list:
        """
        Get all ANAM campaigns.

        Returns
        -------
        list
            List of all campaigns.
        """

        return self._repository.get_all()
