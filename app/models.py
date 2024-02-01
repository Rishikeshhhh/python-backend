from pydantic import BaseModel, EmailStr
from typing import List

class User(BaseModel):
    id: str
    email: EmailStr
    hashed_password: str
    tags: List[str] = []
