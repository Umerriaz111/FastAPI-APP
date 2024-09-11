from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID,uuid4
from enum import Enum
class Gender(str,Enum):
    male="Male"
    female="Female"
class Roles(str,Enum):
    admin="admin"
    student="student"
    user="user"
class User(BaseModel):
    id2: Optional[UUID]=uuid4()
    first_name:str
    last_name: str
    middle_name: Optional[str]
    gender:Gender
    Role:List[Roles]
    