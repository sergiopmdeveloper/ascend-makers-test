from typing import Annotated, Optional

from config.database import get_db_session
from fastapi import APIRouter, Depends, Header, Query, status
from schemas.campaign import CampaignAnamInput, CampaignOutput
from services.campaign_anam_service import CampaignAnamService
from services.campaign_service import CampaignService
from sqlalchemy.orm import Session
from validators.campaign import validate_campaign

campaign_router = APIRouter(prefix="/campaign", tags=["campaign"])


@campaign_router.post(
    "/create", status_code=status.HTTP_201_CREATED, response_model=CampaignOutput
)
def create_campaign(
    name: Annotated[str, Header()],
    anamData: Optional[CampaignAnamInput] = None,
    session: Session = Depends(get_db_session),
) -> CampaignOutput:
    """
    Endpoint to create a new campaign.

    Parameters
    ----------
    name : str
        Campaign name.
    anamData : Optional[CampaignAnamInput], optional
        Campaign Anam data, by default None.
    session : Session
        Database session object.

    Returns
    -------
    CampaignOutput
        Created campaign.
    """

    if anamData:
        validate_campaign(**anamData.dict())

    service = CampaignService(session=session)
    created_campaign = service.create(name=name)

    if anamData:
        anam_service = CampaignAnamService(session=session)
        anamData.campaign_id = created_campaign.id
        anam_status = anam_service.create(anamData)
        created_campaign.created_in_anam = anam_status

    return created_campaign


@campaign_router.get(
    "/get-all", status_code=status.HTTP_200_OK, response_model=list[CampaignOutput]
)
def get_all_campaigns(
    anam_data: bool = Query(False, description="Additionally get ANAM campaigns data."),
    session: Session = Depends(get_db_session),
) -> list[CampaignOutput]:
    """
    Endpoint to get all campaigns.

    Parameters
    ----------
    anam_data : bool
        Flag to include ANAM data.
    session : Session
        Database session object.

    Returns
    -------
    list[CampaignOutput]
        List of campaigns.
    """

    service = CampaignService(session=session)

    return service.get_all(anam_data=anam_data)


@campaign_router.get(
    "/anam/get-all",
    status_code=status.HTTP_200_OK,
    response_model=list[CampaignAnamInput],
)
def get_all_anam_campaigns(
    session: Session = Depends(get_db_session),
) -> list[CampaignAnamInput]:
    """
    Endpoint to get all ANAM campaigns.

    Parameters
    ----------
    session : Session
        Database session object.

    Returns
    -------
    list[CampaignAnamInput]
        List of ANAM campaigns.
    """

    service = CampaignAnamService(session=session)

    return service.get_all()
