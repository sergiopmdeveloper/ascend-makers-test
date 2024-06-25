from models.campaign import Campaign
from schemas.campaign import CampaignOutput
from sqlalchemy.orm import Session, joinedload


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

        campaign_instance = Campaign(name=name)

        self._session.add(campaign_instance)
        self._session.commit()
        self._session.refresh(campaign_instance)

        return CampaignOutput(**campaign_instance.__dict__)

    def get_all(self, anam_data: bool) -> list[CampaignOutput]:
        """
        Get all campaigns.

        Parameters
        ----------
        anam_data : bool
            Flag to include ANAM data.

        Returns
        -------
        list[CampaignOutput]
            List of campaigns.
        """

        if anam_data:
            campaigns = (
                self._session.query(Campaign)
                .options(joinedload(Campaign.campaigns_anam))
                .all()
            )

        else:
            campaigns = self._session.query(Campaign).all()

        return [CampaignOutput(**campaign.__dict__) for campaign in campaigns]
