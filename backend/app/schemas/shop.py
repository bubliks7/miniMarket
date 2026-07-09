from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ShopCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    slug: str
    description: str

class ShopResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    slug: str
    description: str
    created_at: datetime
