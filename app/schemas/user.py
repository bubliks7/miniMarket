from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: str
    password: str
    full_name: str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    email: str
    full_name: str
    role: str
    is_active: bool
    created_at: datetime
