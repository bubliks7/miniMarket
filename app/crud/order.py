from sqlalchemy.orm import Session
from app.models.models import Orders, OrderItems, Products
from app.schemas.order import OrderCreate
from uuid import UUID

def create_order(db: Session, order: OrderCreate, user_id: UUID):
    db_order = Orders(user_id=user_id, total=0.0)
    db.add(db_order)
    db.flush()

    total = 0.0
    for item in order.items:
        product = db.query(Products).filter(Products.id == item.product_id).first()
        db_item = OrderItems(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=product.price
        )
        total += item.quantity * product.price
        db.add(db_item)

    db_order.total = total
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order_by_id(db: Session, id: UUID):
    return db.query(Orders).filter(Orders.id == id).first()

def get_orders_by_user(db: Session, user_id: UUID):
    return db.query(Orders).filter(Orders.user_id == user_id).all()
