from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    description: str
    price: float
    stock: int

class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str
    price: float
    stock: int
    is_active: bool
    created_at: datetime
