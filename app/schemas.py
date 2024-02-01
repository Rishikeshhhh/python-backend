from pydantic import BaseModel, EmailStr
from typing import List

class Item(BaseModel):
    id: str = None  # This will store the string representation of ObjectId
    name: str
    description: str
    
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    tags: List[str] = []

class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: str
    author: str