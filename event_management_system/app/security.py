from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt


pwd_context = CryptContext(
    schemes=["bcrypt_sha256"],
    deprecated="auto"
)


SECRET_KEY = "event_secret_key"
ALGORITHM = "HS256"


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def create_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=60)

    to_encode.update({
        "exp": expire
    })

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )