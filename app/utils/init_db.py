from config.database import engine
from models.campaign import CampaignAscend


def create_tables():
    """
    Creates database tables.
    """

    CampaignAscend.metadata.create_all(bind=engine)
