
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False, index=True)
    category = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    priority = Column(String(20), nullable=False)
    status = Column(String(30), default="Open", nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
