from sqlalchemy.orm import Session
from app.models.models import Users
from app.schemas.user import UserCreate
from app.core.security import hash_password
from uuid import UUID

def create_user(db: Session, user: UserCreate):
    db_user = Users(email=user.email, password=hash_password(user.password), full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()

def get_user_by_id(db: Session, id: UUID):
    return db.query(Users).filter(Users.id == id).first()
