from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.db.session import get_db
from app.core.security import SECRET_KEY, ALGORITHM
from app.models.models import Users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(401, "Nieprawidlowy token")
    except JWTError:
        raise HTTPException(401, "Nieprawidlowy token")
    
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(401, "Uzytkownik nie istnieje")
    
    return user
