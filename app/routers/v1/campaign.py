from config.database import get_db_session
from fastapi import APIRouter, Depends, Query, status
from schemas.campaign import CampaignInput, CampaignOutput
from services.campaign_anam_service import CampaignAnamService
from services.campaign_service import CampaignService
from sqlalchemy.orm import Session
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
    anam_service = CampaignAnamService(session=session)

    created_campaign = service.create(data)
    created_anam_campaign = anam_service.create(data) if anam_campaign_flag else False

    created_campaign.anam_campaign = created_anam_campaign

    return created_campaign


@campaign_router.get("/get-all", response_model=list[CampaignOutput])
def get_all_campaigns(
    session: Session = Depends(get_db_session),
) -> list[CampaignOutput]:
    """
    Endpoint to get all campaigns.

    Parameters
    ----------
    session : Session
        Database session object.

    Returns
    -------
    list[CampaignOutput]
        List of campaigns.
    """

    service = CampaignService(session=session)

    return service.get_all()


@campaign_router.get("/anam/get-all")
def get_all_anam_campaigns(
    session: Session = Depends(get_db_session),
) -> list:
    """
    Endpoint to get all ANAM campaigns.

    Parameters
    ----------
    session : Session
        Database session object.

    Returns
    -------
    list
        List of ANAM campaigns.
    """

    service = CampaignAnamService(session=session)

    return service.get_all()
