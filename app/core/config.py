from datetime import datetime, timedelta, timezone
from jose import jwt

SECRET_KEY = "2d4cf097faf08bc516a453865e84683af4b7a6b321adc69930b70d34f07283ca"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict) -> str:
    