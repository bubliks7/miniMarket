from fastapi import FastAPI
from app.routers.user import router
from app.routers.shop import router as shops_router
from app.routers.product import router as product_router
from app.routers.order import router as order_router

app = FastAPI()

app.include_router(router)
app.include_router(shops_router)
app.include_router(product_router)
app.include_router(order_router)
