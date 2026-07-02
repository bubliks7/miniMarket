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

class orderStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    cancelled = "cancelled"

class Users(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    role = Column(Enum(roleEnum), default=roleEnum.buyer, nullable=False)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    shop = relationship("Shops", back_populates="owner", uselist=False)
    orders = relationship("Orders", back_populates="user")

class Shops(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)
    owner = relationship("Users", back_populates="shop")
    name = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text(), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    products = relationship("Products", back_populates="shop", cascade="all, delete-orphan")

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    shop_id = Column(Integer, ForeignKey("shops.id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text(), nullable=True)
    price = Column(Float(), nullable=False)
    stock = Column(Integer(), default=0)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    shop = relationship("Shops", back_populates="products")
    order_items = relationship("OrderItems", back_populates="products")
    
class Orders(Base):
    __tablename__ = 'orders'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    status = Column(Enum(orderStatus), default=orderStatus.pending)
    total = Column(Float(), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    user = relationship("Users", back_populates="orders")
    items = relationship("OrderItems", back_populates='order', cascade="all, delete-orphan")

class OrderItems(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer(), nullable=False)
    unit_price = Column(Float(), nullable=False)
    order = relationship("Orders", back_populates="items")
    products = relationship("Products", back_populates="order_items")
