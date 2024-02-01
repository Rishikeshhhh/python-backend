from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register_user():
    return {"message": "User registered"}

@router.post("/login")
async def login_user():
    return {"message": "User logged in"}
