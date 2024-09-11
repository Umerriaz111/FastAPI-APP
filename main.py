
from api.user import router
from fastapi import FastAPI
app=FastAPI()
app.include_router(router)