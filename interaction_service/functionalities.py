from typing import List, Optional
from .models import Comment, Like, View
from .schemas import CommentCreate, CommentUpdate, LikeCreate, ViewUpdate
from fastapi import HTTPException

def create_comment(comment: CommentCreate) -> Comment:
    return Comment.create(**comment.dict())

def update_comment(comment_id: int, comment: CommentUpdate, user_id: int) -> Optional[Comment]:
    try:
        comment_obj = Comment.get_by_id(comment_id)
        if user_id != comment_obj.user_id:
            raise HTTPException(status_code=401, detail="Not Authorized") 
        comment_obj.text = comment.text
        comment_obj.save()
        return comment_obj
    except Comment.DoesNotExist:
        return None

def delete_comment(comment_id: int, user_id: int) -> bool:
    try:
        comment = Comment.get_by_id(comment_id)
        if user_id != comment.user_id:
            raise HTTPException(status_code=401, detail="Not Authorized")
        comment.delete_instance()
        return True
    except Comment.DoesNotExist:
        return False

def create_like(like: LikeCreate) -> Like:
    return Like.create(**like.dict())

def get_comments(discussion_id: int) -> List[Comment]:
    return list(Comment.select().where(Comment.discussion == discussion_id))

def get_replies(comment_id: int) -> List[Comment]:
    return list(Comment.select().where(Comment.parent_comment == comment_id))


def get_comment_by_id(comment_id: int) -> Optional[Comment]:
    try:
        return Comment.get_by_id(comment_id)
    except Comment.DoesNotExist:
        return None

def update_view(view_update: ViewUpdate) -> View:
    view,_ = View.get_or_create(discussion_id=view_update.discussion_id, user_id=view_update.user_id)
    print(view.count)
    view.count = int(view.count) + 1
    view.save()
    return view
