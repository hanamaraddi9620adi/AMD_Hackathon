from app.database.postgres import engine
from app.database.base import Base

# Import every model
from app.models.user import User
from app.models.portfolio import Portfolio
from app.models.journal import Journal


def init_db():
    """
    Create all database tables.
    """

    Base.metadata.create_all(bind=engine)