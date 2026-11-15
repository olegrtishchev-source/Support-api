from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class TicketStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    resolved = "resolved"


class TicketCreate(BaseModel):
    subject: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=1)
    customer_email: str


class TicketRead(BaseModel):
    id: int
    subject: str
    description: str
    customer_email: str
    status: TicketStatus
    created_at: datetime
