from sqlalchemy.orm import Session
from app.models.models import Products
from app.schemas.product import ProductCreate

def create_product(db: Session, product: ProductCreate, shop_id: int):
    db_product = Products(name=product.name, stock=product.stock, description=product.description, price=product.price, shop_id=shop_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product_by_id(db: Session, id: int):
    return db.query(Products).filter(Products.id == id).first()

def get_products_by_shop(db: Session, shop: int):
    return db.query(Products).filter(Products.shop_id == shop).all()
