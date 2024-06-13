from passlib.context import CryptContext
import python_jwt as jwt
from datetime import datetime, timedelta
from config.auth import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from user_service.functionalities import get_user_by_id
import bcrypt


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def get_password_hash(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())



