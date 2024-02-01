from fastapi import APIRouter, HTTPException
from ..schemas import UserCreate, User
from ..crud.user import add_user, retrieve_user, update_user, delete_user

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    return await add_user(user.model_dump())

@router.get("/users/{id}", response_model=User)
async def get_user(id: str):
    user = await retrieve_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{id}", response_model=User)
async def update_user_data(id: str, user: UserCreate):
    if await update_user(id, user.model_dump()):
        return await retrieve_user(id)
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{id}", response_model=User)
async def delete_user_data(id: str):
    if await delete_user(id):
        return {"detail": "User deleted"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
