from repositories.campaign_repository import CampaignRepository
from schemas.campaign import CampaignOutput
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

    def create(self, name: str) -> CampaignOutput:
        """
        Create a new campaign.

        Parameters
        ----------
        name : str
            Campaign name.

        Returns
        -------
        CampaignOutput
            Created campaign.
        """

        return self._repository.create(name=name)

    def get_all(self, anam_data: bool = False) -> list[CampaignOutput]:
        """
        Get all campaigns.

        Parameters
        ----------
        anam_data : bool, optional
            Additionally get ANAM campaigns data, by default False.

        Returns
        -------
        CampaignOutput
            List of campaigns.
        """

        return self._repository.get_all(anam_data=anam_data)
