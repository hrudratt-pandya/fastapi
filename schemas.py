from pydantic import BaseModel

"""
If I don't want to show some columns like id then we can create 
pydantic model like below classes & define fields under the class 
which fields you want.
"""

class Blog(BaseModel):  # NOTE: BaseModel: To send body params to the function.
    title:str
    body:str

class ShowBlog(Blog):  # NOTE: we're extending above class because we want same parameters as above
    
    class Config():
        # orm_mode allows your models to be read directly from ORM objects.
        orm_mode = True   # NOTE: By using this site will not show id.

class user(BaseModel):  # NOTE: If we're passing BaseModel then we can costomize which params we want.
    name: str
    email: str
    password: str