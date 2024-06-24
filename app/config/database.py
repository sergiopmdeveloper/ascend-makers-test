import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db_session() -> Generator[Session, None, None]:
    """
    Gets a database session.

    Yields
    ------
    Generator[Session, None, None]
        A database session.
    """

    db_session = SessionLocal()

    try:
        yield db_session
    finally:
        db_session.close()
