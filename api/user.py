import fastapi
from pydantic import BaseModel
from typing import List

router = fastapi.APIRouter()


class User(BaseModel):
    email: str
    is_active: bool


db = []


@router.get("/v1", response_model=List[User])
async def root():
    return db


@router.post("/v1")
async def root2(data: User):
    db.append(data)
    return db
