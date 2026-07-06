from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.shop import ShopCreate, ShopResponse
from app.crud.shop import create_shop, get_all_shops, get_shop_by_id

router = APIRouter(prefix="/shops", tags=["shops"])

@router.get("/", response_model=list[ShopResponse])
def all_shops(db: Session = Depends(get_db)):
    shops = get_all_shops(db)
    return shops

@router.post('/create', response_model=ShopResponse)
def create(shop: ShopCreate, db: Session = Depends(get_db)):
    db_user = create_shop(db, shop, owner_id="0bbbc15d-c306-46b3-8aec-d4db46ff0668")
    return db_user

@router.get("/{shop_id}", response_model=ShopResponse)
def read_shop(shop_id: int, db: Session = Depends(get_db)):
    shop = get_shop_by_id(db, shop_id)
    return shop
