from fastapi import APIRouter, HTTPException, Depends
from typing import List
from config.auth import get_current_user
from user_service.schemas import UserOut
from .schemas import CommentCreate, CommentUpdate, LikeCreate, ViewUpdate, CommentOut,  LikeOut, ViewOut
from .functionalities import create_comment, get_comments, get_replies, update_comment, delete_comment, create_like, update_view

interaction_router = APIRouter()

@interaction_router.post("/comments/", response_model=CommentOut)
def create_comment_endpoint(comment: CommentCreate, current_user: UserOut = Depends(get_current_user)):
    comment.user_id = current_user.id
    return create_comment(comment)

@interaction_router.put("/comments/{comment_id}", response_model=CommentOut)
def update_comment_endpoint(comment_id: int, comment: CommentUpdate, current_user: UserOut = Depends(get_current_user)):
    updated_comment = update_comment(comment_id, comment, current_user.id)
    if updated_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return updated_comment

@interaction_router.delete("/comments/{comment_id}")
def delete_comment_endpoint(comment_id: int, current_user: UserOut = Depends(get_current_user)):
    if not delete_comment(comment_id, current_user.id):
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted successfully"}

@interaction_router.get("/comments/{discussion_id}", response_model=List[CommentOut])
def get_comments_endpoint(discussion_id: int):
    return get_comments(discussion_id)

@interaction_router.get("/replies/{comment_id}", response_model=List[CommentOut])
def get_replies_endpoint(comment_id: int):
    return get_replies(comment_id)

@interaction_router.post("/likes/", response_model=LikeOut)
def create_like_endpoint(like: LikeCreate,current_user: UserOut = Depends(get_current_user)):
    like.user_id = current_user.id
    return create_like(like)


@interaction_router.post("/views/", response_model=ViewOut)
def update_view_endpoint(view: ViewUpdate,current_user: UserOut = Depends(get_current_user)):
    view.user_id=current_user.id
    return update_view(view)
