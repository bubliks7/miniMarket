from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from app.schemas.order_item import OrderItemResponse, OrderItemCreate

class OrderCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    items: list[OrderItemCreate]

class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    status: str
    total: float
    created_at: datetime
    items: list[OrderItemResponse]
