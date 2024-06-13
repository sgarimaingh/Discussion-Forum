from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CreateUser(BaseModel):
    name: str
    mobile_no: str
    email: str
    password: str  

class UpdateUser(BaseModel):
    name: Optional[str] = None
    mobile_no: Optional[str] = None
    email: Optional[str] = None

class UserOut(BaseModel):
    id: int
    name: str
    mobile_no: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes=True
        

class UserLogin(BaseModel):
    email: str
    password: str

class FollowUser(BaseModel):
    followee_id: int
