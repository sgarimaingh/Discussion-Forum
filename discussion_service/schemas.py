from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DiscussionCreate(BaseModel):
    user_id: int
    text: str
    image: Optional[str] = None
    hashtags: Optional[str] = None

class DiscussionUpdate(BaseModel):
    text: Optional[str] = None
    image: Optional[str] = None
    hashtags: Optional[str] = None

class DiscussionOut(BaseModel):
    id: int
    user_id: int
    text: str
    image: Optional[str]
    hashtags: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
