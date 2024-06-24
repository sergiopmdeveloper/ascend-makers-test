import uuid

from config.database import Base
from sqlalchemy import ARRAY, Column, Date, Float, String
from sqlalchemy.dialects.postgresql import UUID


class Campaign(Base):
    """
    Campaign model
    """

    __tablename__ = "campaigns"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    budget = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    keywords = Column(ARRAY(String), nullable=True)
    urls = Column(ARRAY(String), nullable=True)
