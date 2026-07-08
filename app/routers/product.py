from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.product import ProductCreate, ProductResponse
from app.crud.product import create_product, get_products_by_shop, get_product_by_id
from app.core.deps import get_current_user

router = APIRouter(prefix="/products", tags=["products"])

@router.post('/create', response_model=ProductResponse)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = create_product(db, product, shop_id=1)
    return db_product

@router.get("/shop/{shop_id}", response_model=list[ProductResponse])
def read_product_by_shop(shop_id: int, db: Session = Depends(get_db)):
    shop_product = get_products_by_shop(db, shop_id=1)
    return shop_product

@router.get("/{product_id}", response_model=ProductResponse)
def read_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    return product
