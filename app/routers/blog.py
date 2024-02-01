from fastapi import APIRouter, HTTPException
from ..schemas import BlogCreate, Blog
from ..crud.blog import add_blog, retrieve_blogs, update_blog, delete_blog

router = APIRouter()

@router.post("/blogs/", response_model=Blog)
async def create_blog(blog: BlogCreate):
    return await add_blog(blog.model_dump())

@router.get("/blogs/", response_model=list[Blog])
async def get_all_blogs():
    return await retrieve_blogs()

@router.put("/blogs/{id}", response_model=Blog)
async def update_blog_data(id: str, blog: BlogCreate):
    if await update_blog(id, blog.model_dump()):
        return await retrieve_blogs(id)
    else:
        raise HTTPException(status_code=404, detail="Blog not found")

@router.delete("/blogs/{id}", response_model=Blog)
async def delete_blog_data(id: str):
    if await delete_blog(id):
        return {"detail": "Blog deleted"}
    else:
        raise HTTPException(status_code=404, detail="Blog not found")
