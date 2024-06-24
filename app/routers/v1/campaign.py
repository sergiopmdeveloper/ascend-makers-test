from config.database import get_db_session
from fastapi import APIRouter, Depends, status
from schemas.campaign import CampaignInput, CampaignOutput
from services.campaign_service import CampaignService
from sqlalchemy.orm import Session

campaign_router = APIRouter(prefix="/campaign", tags=["campaign"])


@campaign_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_campaign(
    data: CampaignInput, session: Session = Depends(get_db_session)
) -> CampaignOutput:
    """
    Endpoint to create a new campaign.

    Parameters
    ----------
    data : CampaignInput
        Campaign data.
    session : Session
        Database session object.

    Returns
    -------
    CampaignOutput
        Created campaign.
    """

    service = CampaignService(session=session)

    return service.create(data)
