from sqlalchemy import Column, Integer, String, Boolean, Float, Text, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum

from app.db.base import Base 

class roleEnum(str, enum.Enum):
    buyer = "buyer"
    seller = "seller"
    admin = "admin"

class Users(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    rules = Column(Enum(roleEnum), default=roleEnum.buyer, nullable=False)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    shop = relationship("Shops", back_populates="owner", uselist=False)

class Shops(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)
    owner = relationship("Users", back_populates="shop")
    name = Column(String(255))
    slug = Column(String(255), unique=True)
    description = Column(Text(), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
