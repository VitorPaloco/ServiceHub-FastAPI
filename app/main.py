from fastapi import FastAPI
from core.config import middleware
from router import router

app = FastAPI(
    title="Service Hub - Delafoods",
    description="teste da descrição",
    version="1.0.0"
)

middleware(app)
app.include_router(router)