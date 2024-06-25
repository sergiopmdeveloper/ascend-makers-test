import uuid

from config.database import Base
from sqlalchemy import ARRAY, Column, Date, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Campaign(Base):
    """
    Campaign model
    """

    __tablename__ = "campaigns"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    campaigns_anam = relationship("CampaignAnam", back_populates="campaign")


class CampaignAnam(Base):
    """
    CampaignAnam model
    """

    __tablename__ = "campaigns_anam"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    campaign_id = Column(UUID(as_uuid=True), ForeignKey("campaigns.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    budget = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    keywords = Column(ARRAY(String), nullable=True)
    urls = Column(ARRAY(String), nullable=True)
    campaign = relationship("Campaign", back_populates="campaigns_anam")
