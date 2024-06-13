
from config.auth import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import APIRouter, HTTPException, Depends, Response
from typing import List
from .schemas import CreateUser, UpdateUser, UserOut, UserLogin, FollowUser
from .functionalities import create_user, update_user, delete_user, get_users, search_user_by_name, get_user_by_email, follow_user
from .utils import get_password_hash, verify_password
from config.auth import create_access_token, get_current_user
from datetime import timedelta

user_router = APIRouter()

@user_router.post("/signup", response_model=UserOut)
def create_user_endpoint(user: CreateUser):
    user.password = get_password_hash(user.password)
    return create_user(user)

@user_router.put("/{user_id}", response_model=UserOut)
def update_user_endpoint(user_id: int, user: UpdateUser):
    updated_user = update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@user_router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, current_user: UserOut = Depends(get_current_user)):
    if current_user.id != user_id:
        raise HTTPException(status_code=401, detail="Not Authorized")
    if not delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}


@user_router.post("/login")
def login(user: UserLogin, response: Response):
    db_user = get_user_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": str(db_user.id)}, expires_delta=access_token_expires)
    
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return {"message": "Login successful"}

@user_router.get("/", response_model=List[UserOut])
def get_users_endpoint():
    return get_users()

@user_router.get("/search/", response_model=List[UserOut])
def search_user_by_name_endpoint(name: str):
    return search_user_by_name(name)

@user_router.post("/follow")
def follow_user_endpoint(follow: FollowUser, current_user: UserOut = Depends(get_current_user)):  
    if current_user.id==follow.followee_id or not follow_user(current_user.id, follow.followee_id):
        raise HTTPException(status_code=400, detail="Unable to follow user")
    return {"message": "User followed successfully"}

