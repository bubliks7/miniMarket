from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.crud.user import create_user, get_user_by_email
from app.core.token import Token
from app.core.security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/users", tags=["users"])

@router.post('/register', response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, form_data.username)

    if not db_user:
        raise HTTPException(401, "nie znaleziono uzytkownika")

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(401, "zle haslo")
    
    token = create_access_token({"sub": str(db_user.id)})
    return Token(access_token=token, token_type="bearer")
