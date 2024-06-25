from models.campaign import Campaign
from schemas.campaign import CampaignInput, CampaignOutput
from sqlalchemy.orm import Session


class CampaignRepository:
    """
    Repository class for Campaign model.
    """

    def __init__(self, session: Session) -> None:
        """
        Constructor for CampaignRepository class.

        Parameters
        ----------
        session : Session
            Database session object.
        """

        self._session = session

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

        campaign_instance = Campaign(**campaign.dict())

        self._session.add(campaign_instance)
        self._session.commit()
        self._session.refresh(campaign_instance)

        return CampaignOutput(**campaign_instance.__dict__)

    def get_all(self) -> list[CampaignOutput]:
        """
        Get all campaigns.

        Returns
        -------
        CampaignOutput
            List of campaigns.
        """

        campaigns = self._session.query(Campaign).all()

        return [CampaignOutput(**campaign.__dict__) for campaign in campaigns]
