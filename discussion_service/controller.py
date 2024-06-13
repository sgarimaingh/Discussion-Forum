from fastapi import APIRouter, HTTPException, Depends
from typing import List
from .schemas import DiscussionCreate, DiscussionUpdate, DiscussionOut
from user_service.schemas import UserOut
from config.auth import get_current_user
from .functionalities import create_discussion, update_discussion, delete_discussion, get_discussions, get_discussions_by_tag, get_discussions_by_text

discussion_router = APIRouter()

@discussion_router.post("/", response_model=DiscussionOut)
def create_discussion_endpoint(discussion: DiscussionCreate, current_user: UserOut = Depends(get_current_user)):
    if current_user.id != discussion.user_id:
        raise HTTPException(status_code=401, detail="Not Authorized")
    return create_discussion(discussion)

@discussion_router.put("/{discussion_id}", response_model=DiscussionOut)
def update_discussion_endpoint(discussion_id: int, discussion: DiscussionUpdate, current_user: UserOut = Depends(get_current_user)):
    updated_discussion = update_discussion(discussion_id, discussion, current_user.id)
    if updated_discussion is None:
        raise HTTPException(status_code=404, detail="Discussion not found")
    return updated_discussion

@discussion_router.delete("/{discussion_id}")
def delete_discussion_endpoint(discussion_id: int, current_user: UserOut = Depends(get_current_user)):
    if not delete_discussion(discussion_id, current_user.id):
        raise HTTPException(status_code=404, detail="Discussion not found")
    return {"message": "Discussion deleted successfully"}

@discussion_router.get("/", response_model=List[DiscussionOut])
def get_discussions_endpoint():
    return get_discussions()

@discussion_router.get("/tags/{tag}", response_model=List[DiscussionOut])
def get_discussions_by_tag_endpoint(tag: str):
    return get_discussions_by_tag(tag)

@discussion_router.get("/search/", response_model=List[DiscussionOut])
def get_discussions_by_text_endpoint(text: str):
    return get_discussions_by_text(text)
