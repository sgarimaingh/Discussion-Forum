from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    user_id: Optional[int] = None
    discussion_id: int
    text: str
    parent_comment_id: Optional[int] = None
    
class CommentUpdate(BaseModel):
    text: str

class LikeCreate(BaseModel):
    user_id: Optional[int] = None
    comment_id: Optional[int] = None
    discussion_id: Optional[int] = None

class ViewUpdate(BaseModel):
    discussion_id: int
    user_id: Optional[int] = None
    
class CommentOut(BaseModel):
    id: int
    user_id: int
    discussion_id: int
    text: str
    parent_comment_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True


class LikeOut(BaseModel):
    id: int
    user_id: int
    comment_id: Optional[int] = None
    discussion_id: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True

class ViewOut(BaseModel):
    id: int
    discussion_id: int
    user_id: int
    count: int

    class Config:
        orm_mode = True
