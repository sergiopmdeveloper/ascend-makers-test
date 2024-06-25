from config.database import get_db_session
from fastapi import APIRouter, Depends, Query, status
from schemas.campaign import CampaignInput, CampaignOutput
from services.campaign_service import CampaignService
from sqlalchemy.orm import Session
from utils.anam import create_anam_campaign
from validators.campaign import validate_campaign

campaign_router = APIRouter(prefix="/campaign", tags=["campaign"])


@campaign_router.post(
    "/create", status_code=status.HTTP_201_CREATED, response_model=CampaignOutput
)
def create_campaign(
    data: CampaignInput,
    session: Session = Depends(get_db_session),
    anam_campaign_flag: bool = Query(False, description="Create AMAN campaign."),
) -> CampaignOutput:
    """
    Endpoint to create a new campaign.

    Parameters
    ----------
    data : CampaignInput
        Campaign data.
    session : Session
        Database session object.
    anam_campaign_flag : bool
        Flag to create an ANAM campaign.

    Returns
    -------
    CampaignOutput
        Created campaign.
    """

    validate_campaign(**data.dict())

    service = CampaignService(session=session)

    created_campaign = service.create(data)

    if anam_campaign_flag:
        create_anam_campaign(data=data)

    return created_campaign