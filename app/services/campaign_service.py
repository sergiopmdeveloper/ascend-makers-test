from repositories.campaign_repository import CampaignRepository
from schemas.campaign import CampaignInput, CampaignOutput
from sqlalchemy.orm import Session


class CampaignService:
    """
    Service class for Campaign model.
    """

    def __init__(self, session: Session) -> None:
        """
        Constructor for CampaignService class.

        Parameters
        ----------
        session : Session
            Database session object.
        """

        self._repository = CampaignRepository(session)

    def create(self, campaign: CampaignInput) -> CampaignOutput:
        """
        Create a new campaign.

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

    def get_all(self) -> list[CampaignOutput]:
        """
        Get all campaigns.

        Returns
        -------
        CampaignOutput
            List of campaigns.
        """

        return self._repository.get_all()
