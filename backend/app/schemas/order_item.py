from pydantic import BaseModel, ConfigDict
from datetime import datetime

class OrderItemCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    quantity: int

class OrderItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    quantity: int
    unit_price: float
