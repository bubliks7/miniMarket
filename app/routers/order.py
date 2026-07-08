from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.crud.order import create_order, get_order_by_id, get_orders_by_user

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post('/create', response_model=OrderResponse)
def create(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = create_order(db, order, user_id="0bbbc15d-c306-46b3-8aec-d4db46ff0668")
    return db_order

@router.get("/user/{user_id}", response_model=list[OrderResponse])
def read_shop_by_user(user_id: str, db: Session = Depends(get_db)):
    shop_product = get_orders_by_user(db, user_id="0bbbc15d-c306-46b3-8aec-d4db46ff0668")
    return shop_product

@router.get("/{order_id}", response_model=OrderResponse)
def read_order_by_id(order_id: str, db: Session = Depends(get_db)):
    order = get_order_by_id(db, order_id)
    return order
