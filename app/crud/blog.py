from ..database import blog_collection
from bson import ObjectId

# Helper
def blog_helper(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "content": blog["content"],
        "author": blog["author"],
    }

# Retrieve all blogs present in the database
async def retrieve_blogs():
    blogs = []
    async for blog in blog_collection.find():
        blogs.append(blog_helper(blog))
    return blogs

# Add a new blog into the database
async def add_blog(blog_data: dict) -> dict:
    blog = blog_collection.insert_one(blog_data)
    new_blog = await blog_collection.find_one({"_id": blog.inserted_id})
    return blog_helper(new_blog)

# Update a blog with a matching ID
async def update_blog(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if blog:
        updated_blog = await blog_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_blog:
            return True
        return False

# Delete a blog from the database
async def delete_blog(id: str):
    blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if blog:
        await blog_collection.delete_one({"_id": ObjectId(id)})
        return True
