from fastapi import FastAPI
from app.routers.user import router
from app.routers.shop import router as shops_router

app = FastAPI()
app.include_router(router)
app.include_router(shops_router)
