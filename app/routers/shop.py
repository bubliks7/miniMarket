from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.shop import ShopCreate, ShopResponse
from app.crud.shop import create_shop, get_all_shops, get_shop_by_id
from app.core.deps import get_current_user

router = APIRouter(prefix="/shops", tags=["shops"])

@router.get("/", response_model=list[ShopResponse])
def all_shops(db: Session = Depends(get_db)):
    shops = get_all_shops(db)
    return shops

@router.post('/create', response_model=ShopResponse)
def create(shop: ShopCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_shop = create_shop(db, shop, owner_id=current_user.id)
    return db_shop

@router.get("/{shop_id}", response_model=ShopResponse)
def read_shop(shop_id: int, db: Session = Depends(get_db)):
    shop = get_shop_by_id(db, shop_id)
    return shop
