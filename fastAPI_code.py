'''
NOTE:
pip install fastapi
pip install uvicorn
FastAPI is a modern, fast (high-performance),
web framework for building APIs with Python 3.7+
based on standard Python type hints.

Run the code(server) using: uvicorn fastAPI_code:app --reload

http://127.0.0.1:8000/docs to open testing tool
http://127.0.0.1:8000/redoc another testing tool
'''

'''
Points from trainner:
    
'''
# import imp
from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel
# from sympy import im
import uvicorn

app = FastAPI() 

'''
In Python, there are many ways to execute more than one function concurrently
one of the ways is by using asyncio. Async programming allows you to write 
concurrent code that runs in a single thread.
'''

@app.get('/')
# http://127.0.0.1:8000
async def hello_world():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
# http://127.0.0.1:8000/items/5?q=Hrudratt%20here
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/blog")   # you can set default value & field is optional or not.
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):

    if published:
        return f"published with limit {limit} & sort {sort}"
    else:
        return f"Not Published with limit {limit} & sort {sort}"



# post method to create new blog

# blog model # It'll take post method request body
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(blog: Blog):
    return {'data': f'blog is created with title {blog.title} & body is: {blog.body}'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)