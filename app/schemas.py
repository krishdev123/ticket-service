
from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class TicketCreate(BaseModel):
    customer_id: int = Field(gt=0)
    category: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)
    priority: Literal["Low", "Medium", "High"]


class TicketStatusUpdate(BaseModel):
    status: Literal["Open", "In Progress", "Resolved", "Closed"]


class TicketResponse(TicketCreate):
    id: int
    status: str
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
