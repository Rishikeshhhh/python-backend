from ..database import user_collection
from ..token import get_password_hash
from bson import ObjectId

# Helper
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
    }

# Add a new user into the database
async def add_user(user_data: dict) -> dict:
    user_data["hashed_password"] = get_password_hash(user_data["password"])
    del user_data["password"]
    user =  user_collection.insert_one(user_data)
    new_user =  user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False

# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
