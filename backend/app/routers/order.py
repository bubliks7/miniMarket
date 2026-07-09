from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.crud.order import create_order, get_order_by_id, get_orders_by_user
from app.core.deps import get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post('/create', response_model=OrderResponse)
def create(order: OrderCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_order = create_order(db, order, user_id=current_user.id)
    return db_order

@router.get("/user/me", response_model=list[OrderResponse])
def read_shop_by_user(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    shop_product = get_orders_by_user(db, current_user.id)
    return shop_product

@router.get("/{order_id}", response_model=OrderResponse)
def read_order_by_id(order_id: str, db: Session = Depends(get_db)):
    order = get_order_by_id(db, order_id)
    return order
