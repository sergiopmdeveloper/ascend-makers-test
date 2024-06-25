from config.database import engine
from models.campaign import Campaign, CampaignAnam


def create_tables():
    """
    Creates database tables.
    """

    Campaign.metadata.create_all(bind=engine)
    CampaignAnam.metadata.create_all(bind=engine)
