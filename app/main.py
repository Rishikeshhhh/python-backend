from fastapi import FastAPI, HTTPException
from .routers import blog, user, auth
from .database import item_collection
from .schemas import Item

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):
    if not item:
        raise HTTPException(status_code=400, detail="No item provided")

    item_dict = item.model_dump()
    if item_collection.find_one({"name": item_dict["name"]}):
        raise HTTPException(status_code=400, detail="Item already exists")

    item_collection.insert_one(item_dict)
    return item_dict

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    if not item:
        raise HTTPException(status_code=400, detail="No item provided")

    item_dict = item.model_dump()
    if item_collection.find_one({"name": item_dict["name"]}):
        raise HTTPException(status_code=400, detail="Item already exists")

    result = item_collection.insert_one(item_dict)
    item_dict["id"] = str(result.inserted_id)  # Convert ObjectId to string
    return item_dict