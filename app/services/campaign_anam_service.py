from repositories.campaign_anam_repository import CampaignAnamRepository
from schemas.campaign import CampaignInput
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

    def create(self, campaign: CampaignInput) -> bool:
        """
        Create a new ANAM campaign.

        Parameters
        ----------
        campaign : CampaignInput
            Campaign data.

        Returns
        -------
        CampaignOutput
            Created campaign.
        """

        return self._repository.create(campaign)
