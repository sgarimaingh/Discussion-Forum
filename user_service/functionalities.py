from typing import List, Optional
from peewee import DoesNotExist, IntegrityError
from .models import User, Follow
from .schemas import CreateUser, UpdateUser

def create_user(user: CreateUser) -> User:
    return User.create(**user.dict())

def update_user(user_id: int, user: UpdateUser) -> Optional[User]:
    try:
        user_obj = User.get_by_id(user_id)
        if hasattr(user, 'name') and user.name is not None:
            user_obj.name = user.name
        if hasattr(user, 'mobile_no') and user.mobile_no is not None:
            user_obj.mobile_no = user.mobile_no
        if hasattr(user, 'email') and user.email is not None:
            user_obj.email = user.email
        user_obj.save()
        return user_obj
    except DoesNotExist:
        return None

def delete_user(user_id: int) -> bool:
    try:
        user = User.get_by_id(user_id)
        user.delete_instance()
        return True
    except DoesNotExist:
        return False

def get_user_by_id(user_id: int) -> Optional[User]:
    try:
        return User.get_by_id(user_id)
    except DoesNotExist:
        return None

def get_users() -> List[User]:
    return list(User.select())

def search_user_by_name(name: str) -> List[User]:
    return list(User.select().where(User.name.contains(name)))


def get_user_by_email(email: str) -> Optional[User]:
    try:
        return User.get(User.email == email)
    except DoesNotExist:
        return None

def follow_user(follower_id: int, followee_id: int) -> bool:
    try:
        Follow.create(follower=follower_id, followee=followee_id)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False