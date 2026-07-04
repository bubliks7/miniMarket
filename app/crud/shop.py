from sqlalchemy.orm import Session
from app.models.models import Shops
from app.schemas.shop import ShopCreate

def create_shop(db: Session, shop: ShopCreate):
    db_shop = Shops(name=shop.name, slug=shop.slug, description=shop.description)
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return db_shop

def get_shop_by_id(db: Session, id: int):
    return db.query(Shops).filter(Shops.id == id).first()

def get_all_shops(db: Session):
    return db.query(Shops).all()
