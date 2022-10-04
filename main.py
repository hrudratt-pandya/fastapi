'''
COMMENT:
pip install fastapi
pip install uvicorn
FastAPI is a modern, fast (high-performance),
web framework for building APIs with Python 3.7+
based on standard Python type hints.

Run the code(server) using: uvicorn fastAPI_code:app --reload

http://127.0.0.1:8000/docs to open testing tool
http://127.0.0.1:8000/redoc another testing tool
'''


# NOTE: ORM is Object Relational Mapping(Create class name as db name)

# import imp
import email
from typing import Union, Optional
from fastapi import Depends, FastAPI, status, Response, HTTPException
from matplotlib.pyplot import title
import models, schemas, uvicorn
from database import engine, SessionLocal
from typing import List
from sqlalchemy.orm import Session
# from pydantic import BaseModel
# class Blog(BaseModel):  #BaseModel: To send body params to the function.
#     title:str
#     body:str

app = FastAPI()

# create tables
models.Base.metadata.create_all(bind=engine)

# you could use this to create a database session and close it after finishing
def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#MESSAGE: if we're creating something then status code should be 201.


# status module gave us full name suggetion like status.HTTP_201_CREATED.
# @app.post('/blog', status_code=201)
@app.post('/blog', status_code=status.HTTP_201_CREATED) 
def create(request:schemas.Blog, db: Session = Depends(get_db)):
    
    """ This Function Will Add The Data.

    Args:
        request (schemas.Blog): It'll take data from parameter
        db (Session, optional): It'll create session/connection of db.

    Returns:
        new_blog: After adding it'll show data.
    """
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,  db: Session = Depends(get_db)):
    
    """ This function will delete blog from the table.
        If requested id is not available then it'll throw HTTPException.

    Args:
        id (_type_): It'll take id from the parameter('/blog/{id}' from here)
        db (Session, optional): It'll create session/connection of db.

    Returns:
        _type_: Return simple message.
    """
  
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Deleted"


@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,  request: schemas.Blog, db: Session = Depends(get_db)):
    
    """ This function will update blog.
        If requested id is not available then it'll throw HTTPException.

    Args:
        id (_type_): It'll take id from the parameter('/blog/{id}' from here)
        request (schemas.Blog): It'll take data from parameter as per the schemas.
        db (Session, optional): It'll create session/connection of db.

    Returns:
        _type_: Return simple message.
    """

    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not available")
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return "Updated"


# use the response_model to perform the field limiting and serialization.
# If you want to show limited field then you can use response_model.
@app.get('/blog', response_model=List[schemas.ShowBlog]) # we've multiple extries that's why we converted into a list
def all(db: Session = Depends(get_db)):
    
    """ It'll fetch all blog details.

    Args:
        db (Session, optional): It'll create session/connection of db.

    Returns:
        _type_: Returns a all blog details
    """
    
    blog = db.query(models.Blog).all()
    return blog

@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response:Response, db: Session = Depends(get_db)):
 
    """ It'll show particuler id detail which is available in url.
        If requested id is not available then it'll throw HTTPException.

    Args:
        id (_type_): It'll take id from the parameter('/blog/{id}' from here).
        response (Response): If you want to return specific status 
                             then import Response then use 
                             response.status_code.
        db (Session, optional): It'll create session/connection of db.

    Raises:
        HTTPException: If you want to return particular response 
                       status code with message then you can directly
                       use this method.

    Returns:
        _type_: Returns a particular blog.
    """
    
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND    # It'll update status_code
        # return {'detail': f'Blog with id {id} is not available'}
        # NOTE: Insted of using above method we can directly raise error like below.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    return blog


@app.post('/user')
def create_user(request: schemas.user,  db: Session = Depends(get_db)):
    """ Create the user.

    Args:
        request (schemas.user): It'll take data from parameter as per the schemas.
        db (Session, optional): It'll create session/connection of db.

    Returns:
        _type_: Returns data which you've created.
    """
    new_user = models.User(name = request.name, email = request.email, password = request.password)
    # new_user = models.User(request)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request





# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)