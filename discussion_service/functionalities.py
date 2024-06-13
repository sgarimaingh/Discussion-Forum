from fastapi import HTTPException
from typing import List, Optional
from .models import Discussion
from user_service.models import User
from .schemas import DiscussionCreate, DiscussionUpdate

def create_discussion(discussion: DiscussionCreate) -> Discussion:
    #add authorization based on logged in user
    if(User.get_by_id(discussion.user_id) is None):
        return {"message": "User not Present"}
    return Discussion.create(**discussion.dict())

def update_discussion(discussion_id: int, discussion: DiscussionUpdate, user_id: int) -> Optional[Discussion]:
    try:
        discussion_obj = Discussion.get_by_id(discussion_id)
        if user_id != discussion_obj.user_id:
            raise HTTPException(status_code=401, detail="Not Authorized")
        if hasattr(discussion, 'text') and discussion.text is not None:
            discussion_obj.text = discussion.text
        if hasattr(discussion, 'image') and discussion.image is not None:
            discussion_obj.image = discussion.image
        if hasattr(discussion, 'hashtags') and discussion.hashtags is not None:
            discussion_obj.hashtags = discussion.hashtags
        discussion_obj.save()
        return discussion_obj
    except Discussion.DoesNotExist:
        return None

def delete_discussion(discussion_id: int, user_id: int) -> bool:
    try:
        discussion = Discussion.get_by_id(discussion_id)
        if user_id != discussion.user_id:
            raise HTTPException(status_code=401, detail="Not Authorized")
        discussion.delete_instance()
        return True
    except Discussion.DoesNotExist:
        return False

def get_discussions() -> List[Discussion]:
    return list(Discussion.select())

def get_discussions_by_tag(tag: str) -> List[Discussion]:
    return list(Discussion.select().where(Discussion.hashtags.contains(tag)))

def get_discussions_by_text(text: str) -> List[Discussion]:
    return list(Discussion.select().where(Discussion.text.contains(text)))
